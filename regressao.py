# Fonte: https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo

# Descrição:
# A cerveja é uma das bebidas mais democráticas e consumidas no mundo. Não sem razão, é perfeito para quase todas as situações, desde o happy hour até grandes festas de casamento.

# Os dados (amostra) foram coletados em São Paulo - Brasil, em uma área universitária, onde existem algumas festas com grupos de alunos de 18 a 28 anos de idade (média).

# Dados:
# - temp_media - Temperatura Média (°C)
# - consumo - Consumo de Cerveja (litros)


import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import probplot
import matplotlib.pyplot as plt


df_cervejas = pd.read_csv('dados/dados_projeto.csv', sep=';') # [365 rows x 1 columns]


# Estatísticas descritivas
estat_desc = df_cervejas.describe()
#                   Y           X
# count    365.000000  365.000000
# mean   25401.367123   21.226356
# std     4399.142703    3.180108
# min    14343.000000   12.900000
# 25%    22008.000000   19.020000
# 50%    24867.000000   21.380000
# 75%    28631.000000   23.280000
# max    37937.000000   28.860000


# Análise gráfica
# Boxplot - consumo de litros de cerveja
ax = sns.boxplot(data=df_cervejas, x='Y', orient='h', width=0.5)

ax.figure.set_size_inches(12, 6)

ax.set_title('Box plot', fontsize=20)

ax.set_xlabel('Consumo de cerveja (litros)', fontsize=16)

# # Temperatura média
ax = sns.boxplot(data=df_cervejas, x = 'X', orient='h', width=0.5)

ax.figure.set_size_inches(12, 6)

ax.set_title('Box plot', fontsize=20)

ax.set_xlabel('Temperatura média', fontsize=16)


# Regressão linear
Y = df_cervejas.Y

X = sm.add_constant(df_cervejas.X)

regressao = sm.OLS(Y, X).fit()
# OLS Regression Results
# ==============================================================================
# Dep. Variable:                      Y   R-squared:                       0.330
# Model:                            OLS   Adj. R-squared:                  0.328
# Method:                 Least Squares   F-statistic:                     178.9
# Date:                Mon, 26 Sep 2022   Prob (F-statistic):           1.87e-33
# Time:                        18:12:25   Log-Likelihood:                -3506.3
# No. Observations:                 365   AIC:                             7017.
# Df Residuals:                     363   BIC:                             7024.
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const       8528.9073   1275.363      6.687      0.000    6020.880     1.1e+04
# X            794.8825     59.423     13.377      0.000     678.027     911.738
# ==============================================================================
# Omnibus:                       11.300   Durbin-Watson:                   1.623
# Prob(Omnibus):                  0.004   Jarque-Bera (JB):                9.673
# Skew:                           0.324   Prob(JB):                      0.00793
# Kurtosis:                       2.534   Cond. No.                         145.
# ==============================================================================


df_cervejas['Y_previsto'] = regressao.predict()

print(df_cervejas)
