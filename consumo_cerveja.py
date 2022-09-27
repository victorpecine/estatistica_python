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


# Coeficiente de determinação R²
r_quadrado = modelo_reg_lin.score(X_train, y_train)
# 0.6992228468218


# Previsões a partir do modelo
y_previsto = modelo_reg_lin.predict(X_test)


# Coeficiente de determinação R² para as previsões do modelo
r_quadrado_previsao = metrics.r2_score(y_test, y_previsto)
# 0.7614490385510517


# Previsão pontual
X_pontual = X_test[0:1]
#      temp_max  chuva  fds
# 317      30.4   16.4    1

y_pontual = modelo_reg_lin.predict(X_pontual)
# 30931.49446532


# Simulador simples
temp_max = 30.5

chuva = 12.2

fds = 0

X_pontual = [[temp_max, chuva, fds]]

y_pontual = modelo_reg_lin.predict(X_pontual)[0]
# 26159.68166942776
