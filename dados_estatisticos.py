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


# Cruzamento de tabelas
sexo = {0: 'masculino', 1: 'feminino'}

cor = {0:'indigena',
       2: 'branca',
       4: 'preta',
       6: 'amarela',
       8: 'parda',
       9: 'sem declaracao'}

freq_sexo_cor = pd.crosstab(df_ibge['sexo'],
                            df_ibge['cor'])

freq_sexo_cor.rename(index=sexo, columns=cor, inplace=True)
# cor        indigena  branca  preta  amarela  parda
# sexo
# masculino       256   22194   5502      235  25063
# feminino        101    9621   2889      117  10862


porcent_sexo_cor = pd.crosstab(df_ibge['sexo'],
                               df_ibge['cor'],
                               normalize=True) * 100

porcent_sexo_cor.rename(index=sexo, columns=cor, inplace=True)
# cor        indigena     branca     preta   amarela      parda
# sexo
# masculino  0.333160  28.883394  7.160333  0.305830  32.617126
# feminino   0.131442  12.520822  3.759761  0.152264  14.135867


renda_media_sexo_cor =  pd.crosstab(df_ibge['sexo'],
                                    df_ibge['cor'],
                                    aggfunc='mean',
                                    values=df_ibge['renda'])

renda_media_sexo_cor.rename(index=sexo, columns=cor, inplace=True)
# cor           indigena       branca        preta      amarela        parda
# sexo
# masculino  1081.710938  2925.744435  1603.861687  4758.251064  1659.577425
# feminino   2464.386139  2109.866750  1134.596400  3027.341880  1176.758516

renda_media_sexo_cor = renda_media_sexo_cor.round(2)
print(renda_media_sexo_cor)
