def previsao(dados):
    # Bibliotecas necessárias
    import boto3
    import tarfile
    import io
    import os
    import xgboost as xgb
    import tempfile as tmp

    # Inicializa a sessão do boto3, credenciais armazenadas no arquivo ~/.aws/credentials
    s3 = boto3.client('s3')

    # Nome do bucket e caminho do modelo no S3
    bucket_name = 'hotelbuck'
    model_path = 'modelo/model.tar.gz'

    # Carregar o modelo do S3
    try:
        leitura = s3.get_object(Bucket=bucket_name, Key=model_path)
        arquivo = io.BytesIO(leitura['Body'].read())
    except Exception as e:
        raise RuntimeError(f'Erro de leitura do S3: {e}')
    with tmp.NamedTemporaryFile(delete=False) as arquivotemp:
        arquivo_temp = arquivotemp.name

    # Extrair o arquivo tar.gz
    with tarfile.open(fileobj=arquivo, mode="r:gz") as tar:
        for membro in tar.getmembers():
            if "xgboost-model" in membro.name:
                modelo = membro
                break
        with open(arquivo_temp, "wb") as arq:
            arq.write(tar.extractfile(modelo).read())

    # Carregar o modelo usando XGBoost
    model = xgb.Booster()
    model.load_model(arquivo_temp)

    # Apaga o arquivo temporário
    os.remove(arquivo_temp)

    # Converter os dados para o formato DMatrix do XGBoost
    # Ajusta os dados para uma previsão única
    dmat_teste = xgb.DMatrix(dados.reshape(1, -1))  

    # Fazer a previsão
    resposta = model.predict(dmat_teste)
    resposta = int(resposta[0])
    return resposta