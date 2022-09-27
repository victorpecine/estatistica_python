# Fonte do dataset: https://www.kaggle.com/datasets/dongeorge/beer-consumption-sao-paulo


from pyexpat import model
from statistics import mode
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df_consumo = pd.read_csv('dados/consumo_cerveja.csv', sep=';')

# Dataset de teste e treino
# Dividir o dataframe e duas sérias
# Uma com a variável dependente
# Outra com as variáveis independentes

y = df_consumo['consumo']

X = df_consumo[['temp_max', 'chuva', 'fds']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


modelo_reg_lin = LinearRegression().fit(X_train, y_train) # Criação do modelo de treino para regressão linear
