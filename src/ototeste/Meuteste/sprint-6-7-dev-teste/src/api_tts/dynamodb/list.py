import os
import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError

dynamodb = boto3.resource('dynamodb')


def list_dynamodb(event, context):
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])

    try:
        response = table.scan()
        data = response['Items']

        # Continuar escaneando enquanto houver mais dados
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

    except (BotoCoreError, ClientError) as error:
        print(error)
        return {
            "statusCode": 500,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"message": "Error fetching todos from DynamoDB.", "error": str(error)})
        }

    return {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json'},
        "body": json.dumps(data)
    }

