# Estamos estudando o rendimento mensal dos chefes de domicílios com renda até R$ 5.000,00 no Brasil. Nosso supervisor determinou que o erro máximo em relação a média seja de R$ 10,00. Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$ 1.082,79 e que a média populacional é de R$ 1.426,54. Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo? Qual o intervalo de confiança para a média considerando o tamanho de amostra obtido?


import pandas as pd
from scipy.stats import norm
import numpy as np


df_ibge = pd.read_csv('dados.csv') # 76840 linhas, 7 colunas

# Contagem de dados nulos do dataframe
df_ibge.isnull().sum()
# UF                0
# Sexo              0
# Idade             0
# Cor               0
# Anos de Estudo    0
# Renda             0
# Altura            0

# Ajuste dos nomes das colunas
df_ibge.columns = df_ibge.columns.str.lower()

df_ibge.rename(columns={'anos de estudo': 'anos_estudo'}, inplace=True)

df_renda_cincok = df_ibge.query('renda <= 5000').renda # 72109 linhas

desv_padrao = df_renda_cincok.std()
desv_padrao = round(desv_padrao, 2)
# R$ 1082.79

media = df_renda_cincok.mean()
media = round(media, 2)
# R$ 1426.54


# Tamanho da amostra para população infinita
e = 10

confianca = 0.95

area_dist_normal = 0.5 + (0.95 / 2)
# 0.975

z = norm.ppf(area_dist_normal)
# 1.959963984540054

# Tamanho da amostra
n = (z * (desv_padrao / e))**2
n = int(n.round())
# 45039


# Intervalo de confiaça
intervalo = norm.interval(alpha=confianca, loc=media, scale=desv_padrao / np.sqrt(n))
print(intervalo)