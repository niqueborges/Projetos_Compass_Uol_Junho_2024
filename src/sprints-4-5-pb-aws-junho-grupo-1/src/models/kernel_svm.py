# Kernel SVM

# Importação das bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

# Importação do conjunto de dados
dataset = pd.read_csv('src/Tabelas/Hotel Reservations Quantif.csv')

# Definição dos dados de entrada e saída
"""colunas disponíveis: Booking_ID,no_of_adults,no_of_children,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type, 
repeated_guest,no_of_previous_cancellations,no_of_previous_bookings_1,avg_price_per_room,no_of_special_requests,booking_status"""


X = dataset[["no_of_adults","no_of_children","no_of_weekend_nights","no_of_week_nights","type_of_meal_plan",
             "required_car_parking_space","room_type_reserved","arrival_month","arrival_date","market_segment_type",
             "no_of_special_requests","no_of_previous_cancellations","repeated_guest","no_of_previous_bookings_1"]]
y = dataset["label_avg_price_per_room"]


# Divisão do conjunto de dados em Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Treino do modelo Kernel SVM no conjunto de Treino
classifier = SVC(kernel = 'rbf', random_state = 0, C=100.0, gamma= 'auto')
classifier.fit(X_train, y_train)


# Predição dos resultados do conjunto Teste
y_pred = classifier.predict(X_test)

# Calculando as métricas do ajuste
cm = confusion_matrix(y_test, y_pred)
print("Matriz Confusão: \n", cm)
print("\nAcurácia: ",accuracy_score(y_test, y_pred))
#Acurácia: 74,49%