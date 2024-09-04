# Importar as bibliotecas
from fastapi import FastAPI, HTTPException
import previsoes as p
from pydantic import BaseModel
import numpy as np

# Cria o servidor
app = FastAPI()

# Define o conjunto de dados de entrada da API
class Entradas(BaseModel):
    no_of_adults: int
    no_of_childrens: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    type_of_meal_plan: str
    required_car_parking_space: int
    room_type_reserved: str
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    market_segment_type: str
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_1: int
    no_of_special_requests: int

# Funções para conversão dos valores de entrada do tipo string para int
def comida(valor):
    match valor:
        case "Meal Plan 1": return 1
        case "Meal Plan 2": return 2
        case "Meal Plan 3": return 3
        case _: return 0

def quarto(valor):
    match valor:
        case "Room_Type 1": return 1
        case "Room_Type 2": return 2
        case "Room_Type 3": return 3
        case "Room_Type 4": return 4
        case "Room_Type 5": return 5
        case "Room_Type 6": return 6
        case "Room_Type 7": return 7
        case _: return 0

def segmento(valor):
    match valor:
        case "Offline": return 0
        case "Online": return 1
        case "Corporate": return 2
        case "Complementary": return 3
        case "Aviation": return 4
        case _: return 5

# Função para converter formato JSON em array
def converte(dados: Entradas):
    lista = np.array([[
        dados.no_of_adults, dados.no_of_childrens, dados.no_of_weekend_nights, dados.no_of_week_nights, 
        comida(dados.type_of_meal_plan), dados.required_car_parking_space, quarto(dados.room_type_reserved), 
        dados.lead_time, dados.arrival_year, dados.arrival_month, dados.arrival_date, 
        segmento(dados.market_segment_type), dados.repeated_guest, dados.no_of_previous_cancellations, 
        dados.no_of_previous_bookings_1, dados.no_of_special_requests
    ]])
    return lista

# Rota para o POST
@app.post("/api/v1/inference")
def infer(data: Entradas):
    try:
        entrada = converte(data)
        inferencia = p.previsao(entrada)     
        return {"result": inferencia}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Entrada de dados incorreta: {str(e)}")

# Rota para o GET    
@app.get("/")
def raiz():
    return {"mensagem": "API está funcionando"}
