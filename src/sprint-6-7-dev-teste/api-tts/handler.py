import json
import time
import boto3
import os
from contextlib import closing
from botocore.exceptions import BotoCoreError, ClientError
from tempfile import gettempdir


def health(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def lambda_handler(event, context):
     # Desserializando o corpo da requisição
    try:
        body = json.loads(event["body"])
    except (json.JSONDecodeError, KeyError) as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid request. Body must be a valid JSON with 'phrase' key."})
        }

    # Verificando se o campo "phrase" está presente
    if "phrase" not in body or len(body) != 1:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid key in the request body."})
        }

    text = body["phrase"]
    bucket_name = os.environ["BUCKET_NAME"]
    audio_s3_dir = os.environ["AUDIO_S3_DIR"]

    polly = boto3.client(service_name="polly")

    # text = "Teste 1, 2, 3, 4"

    try:
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                            VoiceId="Thiago", Engine="neural")
    except (BotoCoreError, ClientError) as error:
        print(error)
        return {
            "statusCode": 500,
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
                        "body": json.dumps({"message": "Error writing the audio file.", "error": str(error)})
                    }

    else:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "No audio stream returned by Polly."})
        }
    
    # nome do arquivo mp3
    filename = f"{text[:10].replace(' ', '_')}.mp3"

    # Salvar no S3
    try:
        with open(output, "rb") as file:
            boto3.client('s3').upload_fileobj(file, bucket_name, f"{audio_s3_dir}/{filename}", ExtraArgs={'ACL': 'public-read'})
            print("arquivo enviado para o S3")
    except (BotoCoreError, ClientError) as error:
        print("Erro ao enviar o arquivo para o S3:", error)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error uploading the file to S3.", "error": str(error)})
        }
    
    response = {
         "received_phrase": text,
         "url_to_audio": f"https://{bucket_name}.s3.amazonaws.com/{audio_s3_dir}/{filename}",
         "created_audio": time.strftime("%d-%m-%Y %T", time.localtime(time.time())),
         "unique_id": ""
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }