import os
import boto3
from datetime import datetime, timedelta, timezone
import hashlib
# from list import listar_registros

# Função para criar um hash SHA-256 a partir do texto dado, retornando os 16 primeiros caracteres.
def create_hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()[:16]

# Função para criar um registro no banco de dados DynamoDB com base em um texto e uma URL de áudio.
def create_record(text, url_audio):

    # Cria um hash único do texto usando SHA-256.
    unique_hash  = create_hash_sha256(text)

    # Inicializa o recurso DynamoDB.
    dynamodb = boto3.resource('dynamodb')

    # Acessa a tabela DynamoDB a partir da variável de ambiente DB_TABLE_NAME.
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])

    # Gera o timestamp no formato "dia-mês-ano hora:minuto:segundo", ajustado para o fuso horário de UTC-3.
    timestamp = datetime.now(timezone(timedelta(hours=-3))).strftime("%d-%m-%Y %T")

    # Define o item a ser inserido na tabela, incluindo a frase recebida, a URL do áudio e a data de criação.
    item = {
        'received_phrase': text,
        'url_to_audio': url_audio,
        'created_audio': timestamp,
        os.environ['DB_PART_KEY']: unique_hash
    }

    # Insere o item no banco de dados DynamoDB.
    table.put_item(Item=item)
