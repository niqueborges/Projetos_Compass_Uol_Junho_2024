import json
import boto3
import os
from contextlib import closing
from botocore.exceptions import BotoCoreError, ClientError
from tempfile import gettempdir
from api_tts.dynamodb.create import criar_hash_sha256, criar_registro
from api_tts.dynamodb.get import get


def lambda_handler(event, context):
     # Desserializando o corpo da requisição
    try:
        body = json.loads(event["body"])
    except (json.JSONDecodeError, KeyError) as e:
        return {
            "statusCode": 400,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"message": "Invalid request. Body must be a valid JSON with 'phrase' key."})
        }

    # Verificando se o campo "phrase" está presente
    if "phrase" not in body or len(body) != 1:
        return {
            "statusCode": 400,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"message": "Invalid key in the request body."})
        }

    text = body["phrase"].lower().strip()
    bucket_name = os.environ["BUCKET_NAME"]
    audio_s3_dir = os.environ["AUDIO_S3_DIR"]

    # Verificando hashcode do texto recebido no dynamodb

    # Transformar texto em hashcode com hashlib
    hashcode = criar_hash_sha256(text)

    # Verficando se existe esse hashcode no dynamodb, e caso exista retornar os dados para o endpoint
    try:
        if get(hashcode):
            return {
                "statusCode": 200,
                "headers": {'Content-Type': 'application/json'},
                "body": json.dumps(get(hashcode))
            }
    except (BotoCoreError, ClientError) as error:
        print(error)
        return {
            "statusCode": 500,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"message": "Error getting todos from DynamoDB.", "error": str(error)})
        }
              
    else:
        # Gerando áudio do texto recebido com AWS Polly
        polly = boto3.client(service_name="polly")

        # text = "Teste 1, 2, 3, 4"

        try:
            response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                                VoiceId="Thiago", Engine="neural")
        except (BotoCoreError, ClientError) as error:
            print(error)
            return {
                "statusCode": 500,
                "headers": {'Content-Type': 'application/json'},
                "body": json.dumps({"message": "Error synthesizing speech.", "error": str(error)})
            }

        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
                with closing(response["AudioStream"]) as stream:
                    output = os.path.join(gettempdir(), "polly_speech.mp3")

                    try:
                            with open(output, "wb") as file:
                                file.write(stream.read())
                    except IOError as error:
                        print(error)
                        return {
                            "statusCode": 500,
                            "headers": {'Content-Type': 'application/json'},
                            "body": json.dumps({"message": "Error writing the audio file.", "error": str(error)})
                        }

        else:
            return {
                "statusCode": 500,
                "headers": {'Content-Type': 'application/json'},
                "body": json.dumps({"message": "No audio stream returned by Polly."})
            }
        
        # nome do arquivo mp3
        filename = f"{text[:10].replace(' ', '_')}_{hashcode}.mp3"
        url_file = f"https://{bucket_name}.s3.amazonaws.com/{audio_s3_dir}/{filename}"

        # Salvar no S3
        try:
            with open(output, "rb") as file:
                boto3.client('s3').upload_fileobj(file, bucket_name, f"{audio_s3_dir}/{filename}", ExtraArgs={'ACL': 'public-read'})
                print("arquivo enviado para o S3")
        except (BotoCoreError, ClientError) as error:
            print("Erro ao enviar o arquivo para o S3:", error)
            return {
                "statusCode": 500,
                "headers": {'Content-Type': 'application/json'},
                "body": json.dumps({"message": "Error uploading the file to S3.", "error": str(error)})
            }
        
        # Salvar no DynamoDB
        criar_registro(text, url_file)
        
        """ response = {
            "received_phrase": text,
            "url_to_audio": url_file,
            "created_audio": datetime.now(timezone(timedelta(hours=-3))).strftime("%d-%m-%Y %T"),
            "unique_id": hashcode
        } """

        return {
            "statusCode": 200,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps(get(hashcode))
        }