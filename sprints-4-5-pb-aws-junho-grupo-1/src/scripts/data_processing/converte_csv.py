import numpy as np
import pandas as pd

# Importa o arquivo csv original
dataset = pd.read_csv('Hotel Reservations.csv')

# Conversão de type_of_meal_plan
# Not Selected = 0; Meal Plan 1 = 1; Meal Plan 2 = 2; Meal Plan 3 = 3  
val1 = np.sort((dataset['type_of_meal_plan'].unique()))
cval1 = [1, 2, 3, 0]
map1 = dict(zip(val1, cval1))
dataset['type_of_meal_plan'] = dataset['type_of_meal_plan'].replace(map1)

# Conversão de room_type_reserved
# Room_Type 1 = 1; Room_Type 2 = 2; Room_Type 3 = 3; Room_Type 4 = 4; Room_Type 5 = 5; Room_Type 6 = 6; Room_Type 7 = 7
val2 = np.sort((dataset['room_type_reserved'].unique()))
cval2 = list(range(1,len(val2)+1))
map2 = dict(zip(val2, cval2))
dataset['room_type_reserved'] = dataset['room_type_reserved'].replace(map2)

# Conversão de market_segment_type
# Offline = 0; Online = 1; Corporate = 2; Complementary = 3; Aviation = 4
val3 = (dataset['market_segment_type'].unique())
cval3 = [0, 1, 2, 4, 3]
map3 = dict(zip(val3, cval3))
dataset['market_segment_type'] = dataset['market_segment_type'].replace(map3)

# Conversão de booking_status
# Canceled = 0; Not_Canceled = 1
val4 = np.sort((dataset['booking_status'].unique()))
cval4 = list(range(len(val4)))
map4 = dict(zip(val4, cval4))
dataset['booking_status'] = dataset['booking_status'].replace(map4)

# Conversão dos valores do avg_price_per_room na nova coluna label_avg_price_per_room
dataset["label_avg_price_per_room"] = np.where(dataset["avg_price_per_room"]<=85, 1,
                                                np.where(dataset["avg_price_per_room"]<115, 2, 3))

# Eliminação da coluna avg_price_per_room
dataset = dataset.drop('avg_price_per_room', axis=1)

# Criação do arquivo csv modificado
dataset.to_csv('Hotel Reservations Quantif.csv',index=False) 

