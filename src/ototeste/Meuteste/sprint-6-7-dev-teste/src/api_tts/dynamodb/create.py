import os
import boto3
from datetime import datetime, timedelta, timezone
import hashlib
# from list import listar_registros


def criar_hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()[:16]

def criar_registro(text, url_audio):

    # Criar hash usando SHA-256
    hash_unico = criar_hash_sha256(text)

    print(f"Hash único para o texto: {hash_unico}")

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])

    timestamp = datetime.now(timezone(timedelta(hours=-3))).strftime("%d-%m-%Y %T")

    item = {
        'received_phrase': text,
        'url_to_audio': url_audio,
        'created_audio': timestamp,
        os.environ['DB_PART_KEY']: hash_unico
    }

    # write the item to the database
    table.put_item(Item=item)

# List registers
# listar_registros()
