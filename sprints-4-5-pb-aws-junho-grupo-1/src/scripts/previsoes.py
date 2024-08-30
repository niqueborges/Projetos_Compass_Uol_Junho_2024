# Bibliotecas necessárias
import xgboost as xgb
import numpy as np
import tarfile

# Descompacta o arquivo com o modelo
arquivo_modelo = 'model.tar.gz'
with tarfile.open(arquivo_modelo, 'r:gz') as tar:
    tar.extractall()

# Carregar o modelo usando XGBoost
modelo = xgb.Booster()
modelo.load_model('xgboost-model')


# Dados de teste para previsão (ajuste os dados conforme necessário)
# Exemplo de dados de entrada (mesmo formato que usava antes)
'''
"no_of_adults","no_of_children","no_of_weekend_nights","no_of_week_nights","type_of_meal_plan",
"required_car_parking_space","room_type_reserved","lead_time","arrival_year","arrival_month","arrival_date","market_segment_type",
"no_of_special_requests","repeated_guest","no_of_previous_cancellations","no_of_previous_bookings_1"
'''
#2,0,1,2,1,0,1,224,2017,10,2,0,0,0,0,0=>1
#2,0,1,3,1,0,1,34,2017,10,15,1,0,0,0,1=>2
#2,0,1,3,1,0,4,0,2017,9,21,1,0,0,0,1=>3
dados_teste = np.array([2,0,1,3,1,0,1,34,2017,10,15,1,0,0,0,1])

# Converter os dados para o formato DMatrix do XGBoost
# Ajusta os dados para uma previsão única
dmat_teste = xgb.DMatrix(dados_teste.reshape(1, -1))  

# Fazer a previsão
previsao = modelo.predict(dmat_teste)
previsao = int(previsao[0])
print("A reserva é do tipo:", previsao)
