import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import re
import warnings
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
import pickle


import gc
import datetime

color = sns.color_palette()

df_cars = pd.read_csv("argentina_cars.csv", converters={'motor': str})

def preparar_motor(palabra):
    palabra = re.sub('[^0-9.]', ' ', palabra)
    palabra = str.strip(palabra)
    palabra = palabra.split(' ')[0]
    palabra = np.nan if (palabra == '' or palabra == ' ') else palabra
    return palabra

# Pré Processamento
df_cars_2 = df_cars.copy()

valor_dolar = 172.72 # Valor referente a 16/12/2022

# Tornando as moedas no mesmo formato
df_cars_2['money'] = df_cars_2.apply(lambda row: np.round(row['money'] / valor_dolar) \
                                     if row['currency'] == 'pesos' else row['money'], 
                                     axis=1)

df_cars_2.drop(['currency'],axis=1,inplace=True)

# Bibliotecas de Machine Learning
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor

df_cars_3 = df_cars_2.copy()

df_cars_3['motor'] = df_cars_3['motor'].apply(lambda x: preparar_motor(x))
df_cars_3['motor'] = df_cars_3['motor'].astype(float)

le = preprocessing.LabelEncoder()

df_cars_3['color'] = le.fit_transform(df_cars_3['color'])
df_cars_3['fuel_type'] = le.fit_transform(df_cars_3['fuel_type'])
df_cars_3['gear'] = le.fit_transform(df_cars_3['gear'])
df_cars_3['body_type'] = le.fit_transform(df_cars_3['body_type'])

df_cars_3 = df_cars_3[df_cars_3['money'] < 100000]
df_cars_3 = df_cars_3[df_cars_3['kilometres'] < 250000]
df_cars_3 = df_cars_3[df_cars_3['year'] >= 2000]
df_cars_3.shape

df_cars_4 = df_cars_3.drop(['brand', 'model', 'body_type',],axis=1)

df_cars_4 = df_cars_4.dropna()

X = df_cars_4.drop(['money'], axis=1).values
y = df_cars_4['money']

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)

model = RandomForestRegressor(max_depth=9,random_state=10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = round(metrics.mean_squared_error(y_test, y_pred), 5)
rmse = round(np.sqrt(mse), 3)
r2_value = round(metrics.r2_score(y_test, y_pred), 5)

import pickle

# Guardar el modelo entrenado en un archivo .pkl
with open("random_forest_model.pkl", "wb") as f:
    pickle.dump(model, f)
