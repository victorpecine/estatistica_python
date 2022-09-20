# Em nosso dataset temos os rendimento dos chefes de domicílio obtidos da Pesquisa Nacional por Amostra de Domicílios - PNAD no ano de 2015. Um problema bastante conhecido em nosso país diz respeito a desigualdade de renda, principalmente entre homens e mulheres.

# Duas amostras aleatórias, uma de 500 homens e outra com 500 mulheres, foram selecionadas em nosso dataset. Com o objetivo de comprovar tal desigualdade, teste a igualdade das médias entre estas duas amostras com um nível de significância de 1%.


import pandas as pd
import numpy as np
from scipy.stats import norm


df_ibge = pd.read_csv('dados/dados.csv') # 76840 linhas, 7 colunas

# Contagem de dados nulos do dataframe
df_ibge.isnull().sum()

# Ajuste dos nomes das colunas
df_ibge.columns = df_ibge.columns.str.lower()

df_ibge.rename(columns={'anos de estudo': 'anos_estudo'}, inplace=True)


# Amostras de renda por sexo
homens = df_ibge.query('sexo == 0').sample(n=500, random_state=101).renda

mulheres = df_ibge.query('sexo == 1').sample(n=500, random_state=101).renda


media_amostra_M = mulheres.mean()
# 1357.528

desvio_padrao_amostra_M = mulheres.std()
# 1569.9011907484578


media_amostra_H = homens.mean()
# 2142.608

desvio_padrao_amostra_H = homens.std()
# 2548.050802499875


significância = 0.01

confianca = 1 - significância

n_M = 500

n_H = 500

d_0 = n_H - n_M # Diferença entre as medias


# Hipóteses para teste unicaudal superior
# u1 = média de renda homens
# u2 = media de renda mulheres

# Hipótese nula H0 -> n_H - n_M <= 0
# H1 -> n_H - n_M > 0

if n_H - n_M <= d_0:
    print('Teste unicaudal superior confirmado pela hipótese H0')
else:
    print('Teste unicaudal superior desconsiderado pela hipótese H0')

# Teste unicaudal superior confirmado pela hipótese H0


probabilidade = confianca
# 0.99

z_alpha = norm.ppf(probabilidade)
# 2.3263478740408408


# Cálculo da estatística-teste e verificação desse valor com as áreas de aceitação e rejeição do teste
numerador = (media_amostra_H - media_amostra_M) - d_0

denominador = np.sqrt((desvio_padrao_amostra_H ** 2 / n_H) + (desvio_padrao_amostra_M ** 2 / n_M))

z = numerador / denominador
# 5.86562005776475


# Teste valor crítico z
if z >= z_alpha:
    print('Hipótese nula H0 rejeitada pelo valor crítico z\nA média de renda dos homens é maior que a média de renda das mulheres')
else:
    print('Hipótese nula H0 aceita pelo valor crítico z\nA média de renda dos homens é menor ou igual à média de renda das mulheres')

# A média de renda dos homens é maior que a média de renda das mulheres
