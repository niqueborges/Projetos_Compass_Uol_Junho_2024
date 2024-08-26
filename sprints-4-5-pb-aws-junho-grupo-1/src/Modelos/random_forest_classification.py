# Random Forest Classificação

# Importação das bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


# Importação do conjunto de dados
dataset = pd.read_csv('src/Tabelas/Hotel Reservations Quantif.csv')

#  Definição dos dados de entrada e saída
"""colunas disponíveis: Booking_ID,no_of_adults,no_of_children,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type,
repeated_guest,no_of_previous_cancellations,no_of_previous_bookings_1,avg_price_per_room,no_of_special_requests,booking_status"""


X = dataset[["no_of_adults","no_of_children","no_of_weekend_nights","no_of_week_nights","type_of_meal_plan",
             "required_car_parking_space","room_type_reserved","lead_time","arrival_year","arrival_month","arrival_date","market_segment_type",
             "no_of_special_requests","repeated_guest","no_of_previous_cancellations","no_of_previous_bookings_1"]]
y = dataset["label_avg_price_per_room"]


# Divisão do conjunto de dados em Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Treino do modelo Random Forest Classification no conjunto de Treino
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'gini', random_state = 0)
classifier.fit(X_train, y_train)
print("Acurácia dos dados treino: ",classifier.score(X_train,y_train))


# Predição dos resultados do conjunto Teste
y_pred = classifier.predict(X_test)
#print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# Calculando as métricas do ajuste
cm = confusion_matrix(y_test, y_pred)
print("\nMatriz Confusão: \n", cm)
print("\nAcurácia dos dados teste: ",accuracy_score(y_test, y_pred))

"""
Acurácia com "no_of_adults","no_of_children","no_of_weekend_nights","no_of_week_nights","type_of_meal_plan",
             "required_car_parking_space","room_type_reserved","lead_time","arrival_month","market_segment_type",
             "no_of_special_requests" => 81,43%

Acurácia com "no_of_adults","no_of_children","no_of_weekend_nights","no_of_week_nights","type_of_meal_plan",
             "required_car_parking_space","room_type_reserved","lead_time","arrival_month","arrival_date","arrival_year","market_segment_type",
             "no_of_special_requests","no_of_previous_cancellations","repeated_guest","no_of_previous_bookings_1" => 86,47%

"""
