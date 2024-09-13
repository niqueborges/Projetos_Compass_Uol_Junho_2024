import json
import os
import boto3
from api_tts.dynamodb.get import get

dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

def find_file_with_id(file_id):
    # Listar objetos na pasta específica do bucket
    response = s3_client.list_objects_v2(
        Bucket=os.environ['BUCKET_NAME'],
        Prefix=os.environ['AUDIO_S3_DIR']
    )

    # Filtrar arquivos que terminam com o ID especificado
    for obj in response['Contents']:
        file_name = obj['Key']

        if file_id in file_name:
            return file_name

    return  # Retorna None se nenhum arquivo foi encontrado


def delete(event, context):
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    user_id = event['pathParameters']['id']

    # fetch todo from the database
    result = get(user_id)

    if result:

        # delete the todo from the database
        table.delete_item(
            Key={
                os.environ['DB_PART_KEY']: user_id
            }
        )

        # Find the file in S3 with the specified ID
        file_name = find_file_with_id(user_id)

        # Delete the audio file from the S3 bucket
        if file_name:
            s3_client.delete_object(
                Bucket=os.environ['BUCKET_NAME'],
                Key=file_name
            )

        # create a response
        response = {
            "statusCode": 200,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"message": f"File with ID {user_id} deleted."})
        }

        return response
    
    else:
        return {
            "statusCode": 400,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"message": "ID Not found."})
        }