import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import normaltest


df_ibge = pd.read_csv('dados/dados.csv') # 76840 linhas, 7 colunas

# Contagem de dados nulos do dataframe
df_ibge.isnull().sum()

# Ajuste dos nomes das colunas
df_ibge.columns = df_ibge.columns.str.lower()

df_ibge.rename(columns={'anos de estudo': 'anos_estudo'}, inplace=True)


significancia = 0.05


# Teste da hipótese nula H0 para renda
stat_test, p_valor = normaltest(df_ibge['altura'])

if p_valor <= significancia:
    print('A amostra não é proveniente de uma distribuição normal\np_valor = {}\nDesconsiderar a hipótese nula H0'.format(p_valor))
else:
    print('A amostra é proveniente de uma distribuição normal e seu p_valor é {}'.format(p_valor))
