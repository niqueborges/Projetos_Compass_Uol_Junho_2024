import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Gerar dados de exemplo
data = {
    'feature1': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 10,
    'feature2': [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0] * 10,
    'feature3': [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0] * 10,
    'target': [0, 1] * 50
}
df = pd.DataFrame(data)

# Definir as características e o alvo
X = df[['feature1', 'feature2', 'feature3']]
y = df['target']

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Salvar o modelo
model_path = 'model.pkl'
accuracy_path = 'accuracy.txt'
try:
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)
    with open(accuracy_path, 'w') as file:
        file.write(f"{accuracy:.4f}")
    print(f'Modelo salvo em {model_path}')
    print(f'Acurácia salva em {accuracy_path}')
except Exception as e:
    print(f'Erro ao salvar o modelo ou a acurácia: {e}')
