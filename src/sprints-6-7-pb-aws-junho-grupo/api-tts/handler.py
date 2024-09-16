import json
import hashlib
from datetime import datetime
from utils.dynamo_utils import check_if_exists_in_dynamodb, save_to_dynamodb
from utils.polly_utils import generate_audio
from utils.s3_utils import upload_audio_to_s3

def health(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Go Serverless! Your function executed successfully!",
            "input": event
        })
    }

def v1_description(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "TTS API version 1."
        })
    }

def handle_request(event, context):
    try:
        body = json.loads(event['body'])
        phrase = body.get('phrase')

        if not phrase:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Phrase is required"})
            }

        # Gerar hash da frase
        hash_id = hashlib.sha256(phrase.encode('utf-8')).hexdigest()

        # Verificar no DynamoDB
        existing_item = check_if_exists_in_dynamodb(hash_id)
        if existing_item:
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "received_phrase": existing_item['phrase'],
                    "url_to_audio": existing_item['audio_url'],
                    "created_audio": existing_item['timestamp'],
                    "unique_id": hash_id
                })
            }

        # Gerar áudio via Polly
        audio_stream = generate_audio(phrase)
        audio_filename = f"{hash_id}.mp3"

        # Upload para S3
        bucket_name = 'your-s3-bucket-name'  # Substitua pelo nome do seu bucket
        audio_url = upload_audio_to_s3(audio_stream, bucket_name, audio_filename)

        # Salvar no DynamoDB
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_to_dynamodb(hash_id, phrase, audio_url, timestamp)

        # Resposta
        return {
            "statusCode": 200,
            "body": json.dumps({
                "received_phrase": phrase,
                "url_to_audio": audio_url,
                "created_audio": timestamp,
                "unique_id": hash_id
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
