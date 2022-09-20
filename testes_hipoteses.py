# Um famoso fabricante de refrigerantes alega que uma lata de 350 ml de seu principal produto contém, no máximo, 37 gramas de açúcar. Esta alegação nos leva a entender que a quantidade média de açúcar em uma lata de refrigerante deve ser igual ou menor que 37 g.

# Um consumidor desconfiado e com conhecimentos em inferência estatística resolve testar a alegação do fabricante e seleciona, aleatóriamente, em um conjunto de estabelecimentos distintos, uma amostra de 25 latas do refrigerante em questão. Utilizando o equipamento correto o consumidor obteve as quantidades de açúcar em todas as 25 latas de sua amostra. 

# Assumindo que essa população se distribua aproximadamente como uma normal e considerando um nível de significância de 5%, é possível aceitar como válida a alegação do fabricante?


import pandas as pd
from scipy.stats import t as t_student
import numpy as np
from statsmodels.stats.weightstats import DescrStatsW


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


amostra = [37.27, 36.42, 34.84, 34.60, 37.49, 
           36.53, 35.49, 36.90, 34.52, 37.30, 
           34.99, 36.55, 36.29, 36.06, 37.42, 
           34.47, 36.70, 35.86, 36.80, 36.92, 
           37.04, 36.39, 37.32, 36.64, 35.45]

df_amostra = pd.DataFrame(amostra, columns=['amostra'])

media_amostra = df_amostra.mean()[0]
# 36.250400000000006

desvio_padrao_amostra = df_amostra.std()[0]
# 0.9667535018469453

media = 37

significancia = 0.05

confianca = 1 - significancia

n = 25

graus_de_liberdade = n - 1

t_alpha = t_student.ppf(confianca, graus_de_liberdade)
# 1.7108820799094275


# Cálculo de estatística-teste para área de aceitação e rejeição
t = (media_amostra - media) / (desvio_padrao_amostra / np.sqrt(n))
# -3.876893119952045


# Hipótese H0
# u <= 37

# Hipótese H1
# u > 37

# Teste valor crítico t
if t >= t_alpha:
    print('Hipótese H0 rejeitada pelo valor crítico t\nAs latas de refrigerante podem ter mais de 37 g de açúcar')
else:
    print('Hipótese H0 aceita pelo valor crítico t\nAs latas de refrigerante não têm mais de 37 g de açúcar')

# Hipótese H0 aceita
# As latas de refrigerante não têm mais de 37 g de açúcar


# Teste valor p_valor
test = DescrStatsW(amostra)

t, p_valor, grau_liberdade = test.ttest_mean(value=media, alternative='larger')
# t = -3.8768931199520447
# p_valor = 0.999640617030382
# grau_liberdade = 24.0

if p_valor <= significancia:
    print('Hipótese H0 rejeitada pelo valor p\nAs latas de refrigerante podem ter mais de 37 g de açúcar')
else:
    print('Hipótese H0 aceita pelo valor p\nAs latas de refrigerante não têm mais de 37 g de açúcar')

# Hipótese H0 aceita pelo valor p
# As latas de refrigerante não têm mais de 37 g de açúcar
