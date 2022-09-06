from dis import dis
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

# Ajuste dos nomes das colunas
df_ibge.columns = df_ibge.columns.str.lower()

df_ibge.rename(columns={'anos de estudo': 'anos_estudo'}, inplace=True)


# Análises iniciais
idade_min = df_ibge['idade'].min() # 13

idade_max = df_ibge['idade'].max() # 99

altura_min = df_ibge['altura'].min() # 1.339244614 metros

altura_max = df_ibge['altura'].max() # 2.028496765 metros

freq_sexo = df_ibge['sexo'].value_counts()
# 0    53250 - homens
# 1    23590 - mulheres

porcent_sexo = df_ibge['sexo'].value_counts(normalize=True) * 100
# 0    69.299844%
# 1    30.700156%

# Distribuição de frequência
dist_freq_sexo = pd.DataFrame({'frequencia_sexo': freq_sexo, 'porcentual_sexo':porcent_sexo})

dist_freq_sexo.rename_axis('sexo', axis='columns', inplace=True)
dist_freq_sexo.rename(index={0: 'masculino', 1: 'feminino'}, inplace=True)

print(dist_freq_sexo)

dist_freq_sexo.to_csv('dados/df_sexo.csv')
