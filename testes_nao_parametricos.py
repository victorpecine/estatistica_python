# Um novo tratamento para acabar com o hábito de fumar está sendo empregado em um grupo de 35 pacientes voluntários. De cada paciente testado foram obtidas as informações de quantidades de cigarros consumidos por dia antes e depois do término do tratamento. Assumindo um nível de confiança de 95% é possível concluir que, depois da aplicação do novo tratamento, houve uma mudança no hábito de fumar do grupo de pacientes testado?


import pandas as pd
from scipy.stats import norm
import numpy as np


fumo = {
    'antes': [39, 25, 24, 50, 13, 52, 21, 29, 10, 22, 50, 15, 36, 39, 52, 48, 24, 15, 40, 41, 17, 12, 21, 49, 14, 55, 46, 22, 28, 23, 37, 17, 31, 49, 49],
    'depois': [16, 8, 12, 0, 14, 16, 13, 12, 19, 17, 17, 2, 15, 10, 20, 13, 0, 4, 16, 18, 16, 16, 9, 9, 18, 4, 17, 0, 11, 14, 0, 19, 2, 9, 6]
}

significancia = 0.05

confianca = 1 - significancia

n = 35

df_fumo = pd.DataFrame(fumo)

media_antes = df_fumo['antes'].mean()
# 31.857142857142858

media_depois = df_fumo['depois'].mean()
# 11.2


# Formulação das hipóteses
# H0 -> media_antes = media_depois
# H1 -> media_antes > media_depois


probabilidade = (0.5 + (confianca / 2))
# 0.975

z_alpha_2 = norm.ppf(probabilidade)
# 1.959963984540054


df_fumo['diferenca'] = df_fumo['depois'] - df_fumo['antes']

df_fumo['|diferenca|'] = df_fumo['diferenca'].abs()

df_fumo.sort_values(by = '|diferenca|', inplace = True)

df_fumo['#'] = range(1, len(df_fumo) + 1)


df_media_grupos = df_fumo[['|diferenca|', '#']].groupby(['|diferenca|']).mean()

df_media_grupos.rename(columns={'#': 'media_'}, inplace=True)

df_media_grupos.reset_index(inplace=True) # Cria index


df_fumo.drop(['#'], axis = 1, inplace = True) # Apaga a coluna #

df_fumo = df_fumo.merge(df_media_grupos, left_on='|diferenca|', right_on='|diferenca|', how = 'left') # Left join utilizando |diferenca|


df_fumo['media_ (+)'] = df_fumo.apply(lambda x: x.media_ if x.diferenca > 0 else 0, axis = 1)

df_fumo['media_ (-)'] = df_fumo.apply(lambda x: x.media_ if x.diferenca < 0 else 0, axis = 1)

df_fumo.drop(['media_'], axis = 1, inplace = True)


# T = menor das somas de medias de mesmo sinal
T = min(df_fumo['media_ (+)'].sum(), df_fumo['media_ (-)'].sum())
# 22.0

mu_T = (n * (n + 1)) / 4
# 315.0

sigma_T = np.sqrt((n * (n + 1) * ((2 * n) + 1)) / 24)
# 61.053255441458646


# Z teste
Z = (T - mu_T) / sigma_T
# -4.799088891843698


# Teste valor crítico z
if Z >= z_alpha_2 or Z <= -abs(z_alpha_2):
    print('Hipótese H0 rejeitada pelo valor crítico z\nA média de cigarros antes do teste é maior que a média após o teste')
else:
    print('Hipótese H0 aceita pelo valor crítico z\nA média de cigarros antes do teste é menor que a média após o teste')