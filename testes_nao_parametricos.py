# Em nosso dataset temos os rendimento dos chefes de domicílio obtidos da Pesquisa Nacional por Amostra de Domicílios - PNAD no ano de 2015. Um problema bastante conhecido em nosso país diz respeito a desigualdade de renda, principalmente entre homens e mulheres.

# Duas amostras aleatórias, uma de 6 homens e outra com 8 mulheres, foram selecionadas em nosso dataset. Com o objetivo de comprovar tal desigualdade teste a igualdade das médias entra estas duas amostras com um nível de significância de 5%.


import pandas as pd
from scipy.stats import t as t_student, mannwhitneyu
import numpy as np


df_ibge = pd.read_csv('dados/dados.csv') # 76840 linhas, 7 colunas

# Contagem de dados nulos do dataframe
df_ibge.isnull().sum()

# Ajuste dos nomes das colunas
df_ibge.columns = df_ibge.columns.str.lower()

df_ibge.rename(columns={'anos de estudo': 'anos_estudo'}, inplace=True)


mulheres = df_ibge.query('sexo == 1 and renda > 0').sample(n=8, random_state=101).renda

homens = df_ibge.query('sexo == 0 and renda > 0').sample(n=6, random_state=101).renda


media_amostra_M = mulheres.mean()
# 1090.75

media_amostra_H = homens.mean()
# 1341.6666666666667


significancia = 0.05

confianca = 1 - significancia

n_1 = len(homens) # Número de elementos do menor grupo

n_2 = len(mulheres) # Número de elementos do maior grupo


# Hipóteses
# H0 -> media_amostra_M = media_amostra_H
# H1 -> media_amostra_M < media_amostra_H

# Deve-se optar pela distribuição t de Student, já que nada é mencionado sobre a distribuição da população, o desvio padrão populacional é desconhecido e o número de elementos investigados é menor que 30.


graus_de_liberdade = n_1 + n_2 - 2


tabela_t_student = pd.DataFrame(
    [], 
    index=[i for i in range(1, 31)],
    columns = [i / 100 for i in range(10, 0, -1)]
)

for index in tabela_t_student.index:
    for column in tabela_t_student.columns:
        tabela_t_student.loc[index, column] = t_student.ppf(1 - float(column) / 2, index)

index=[('Graus de Liberdade (n - 1)', i) for i in range(1, 31)]
tabela_t_student.index = pd.MultiIndex.from_tuples(index)

columns = [("{0:0.3f}".format(i / 100), "{0:0.3f}".format((i / 100) / 2)) for i in range(10, 0, -1)]
tabela_t_student.columns = pd.MultiIndex.from_tuples(columns)

tabela_t_student.rename_axis(['Bicaudal', 'Unicaudal'], axis=1, inplace = True)

# print(tabela_t_student[10:13])

t_alpha = t_student.ppf(significancia, graus_de_liberdade)
# -1.78


df_homens = pd.DataFrame(homens)
df_homens['sexo'] = 'homens'

df_mulheres = pd.DataFrame(mulheres)
df_mulheres['sexo'] = 'mulheres'


df_sexo = df_homens.append(df_mulheres)

df_sexo.reset_index(inplace = True, drop = True)

df_sexo.sort_values(by = 'renda', inplace = True)

df_sexo['ordenacao'] = range(1, len(df_sexo) + 1) # Variável de ordenação


df_ordenado = df_sexo[['renda', 'ordenacao']].groupby(['renda']).mean()

df_ordenado.reset_index(inplace = True)


df_sexo.drop(['ordenacao'], axis = 1, inplace = True)

df_sexo = df_sexo.merge(df_ordenado, left_on='renda', right_on='renda', how = 'left') # Left join utilizando a renda


# R_1 = soma dos postos do grupo n_1
# R_2 = soma dos postos do grupo n_2

Temp = df_sexo[['sexo', 'ordenacao']].groupby('sexo').sum()
# homens 61.0
# mulheres 44.0

R_1 = Temp.loc['homens'][0]

R_2 = Temp.loc['mulheres'][0]


u_1 = n_1 * n_2 + ((n_1 * (n_1 + 1)) / (2)) - R_1


u_1 = n_1 * n_2 + ((n_1 * (n_1 + 1)) / (2)) - R_1
# 8.0

u_2 = n_1 * n_2 + ((n_2 * (n_2 + 1)) / (2)) - R_2
# 40.0

u = min(u_1, u_2)

mu_u = (n_1 * n_2) / 2

sigma_u = np.sqrt(n_1 * n_2 * (n_1 + n_2 + 1) / 12)

Z = (u - mu_u) / sigma_u

Z.round(2)
# -2.065591117977289


# Teste pelo valor crítico t para caso unicaudal inferior
if Z <= t_alpha:
    print('Hipótese nula rejeitada pelo teste do valor crítico t\nA média de renda das mulheres é menor que a média de renda dos homens')
else:
    print('Hipótese nula aceita pelo teste do valor crítico t\nA média de renda das mulheres é igual a média de renda dos homens')

# Hipótese nula rejeitada pelo teste do valor crítico t
# A média de renda das mulheres é menor que a média de renda dos homens


# Teste pelo valor p
u, p_valor = mannwhitneyu(mulheres, homens, alternative='less')
# u = 8.0
# p_valor = 0.022221119551528605

if p_valor <= significancia:
    print('*' * 50)
    print('Hipótese nula rejeitada pelo teste do valor p\nA média de renda das mulheres é menor que a média de renda dos homens')
    print('*' * 50)
else:
    print('*' * 50)
    print('Hipótese nula aceita pelo teste do valor p\nA média de renda das mulheres é igual a média de renda dos homens')
    print('*' * 50)

# Hipótese nula rejeitada pelo teste do valor p
# A média de renda das mulheres é menor que a média de renda dos homens
