import os

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(id):
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])

    # delete the todo from the database
    table.delete_item(
        Key={
            'unique_id': id
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response

delete('1caa0322dd26307c')