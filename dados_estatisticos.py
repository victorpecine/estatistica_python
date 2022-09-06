import pandas as pd


df_ibge = pd.read_csv('dados/dados.csv') # 76840 linhas, 7 colunas

# Contagem de dados nulos do dataframe
df_ibge.isnull().sum()
# UF                0
# Sexo              0
# Idade             0
# Cor               0
# Anos de Estudo    0
# Renda             0
# Altura            0

# Ajuste de nomes das colunas
df_ibge.columns = df_ibge.columns.str.lower()

df_ibge.rename(columns={'anos de estudo': 'anos_estudo'}, inplace=True)

print(df_ibge)
