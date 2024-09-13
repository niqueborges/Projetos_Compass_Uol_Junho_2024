import os
import boto3
from collections import OrderedDict

dynamodb = boto3.resource('dynamodb')


def get(hashcode):
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            os.environ['DB_PART_KEY']: hashcode
        }
    )

    # print(result)

    if 'Item' in result:
        item = result['Item']
        ordered_item = OrderedDict([
        ('received_phrase', item.get('received_phrase')),
        ('url_to_audio', item.get('url_to_audio')),
        ('created_audio', item.get('created_audio')),
        (os.environ['DB_PART_KEY'], item.get(os.environ['DB_PART_KEY']))
    ])
        return ordered_item
    
    return  # Retorna None se nenhum todo for encontrado no DynamoDB

# if get('t'):
#     print(get('3882393f8d683d23'))