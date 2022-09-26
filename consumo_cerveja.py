import pandas as pd


df_consumo = pd.read_csv('dados/consumo_cerveja.csv', sep=';')

# Tabela de estatísticas descritivas
estats_descits = df_consumo.describe()

print(estats_descits)
