from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
import os

app = FastAPI()

# Função para carregar o modelo
def load_model():
    model_path = 'model.pkl'
    if not os.path.exists(model_path):
        raise HTTPException(status_code=500, detail="Modelo não encontrado!")
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Função para carregar a precisão
def load_accuracy():
    accuracy_path = 'accuracy.txt'
    if not os.path.exists(accuracy_path):
        raise HTTPException(status_code=500, detail="Precisão não encontrada!")
    with open(accuracy_path, 'r') as file:
        accuracy = file.read().strip()
    return accuracy

# Carregar o modelo ao iniciar a aplicação
try:
    model = load_model()
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro ao carregar o modelo: {str(e)}")

# Definir o modelo de entrada para a previsão
class PredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(input_data: PredictionInput):
    data = pd.DataFrame([input_data.dict()])
    try:
        # Fazer a previsão
        prediction = model.predict(data)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        # Tratar e registrar erros
        raise HTTPException(status_code=400, detail=f"Erro ao fazer a previsão: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "API está funcionando"}

@app.get("/accuracy")
def get_accuracy():
    try:
        accuracy = load_accuracy()
        return {"accuracy": accuracy}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao carregar a precisão: {str(e)}")
