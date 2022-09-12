# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma distribuição aproximadamente normal, com média 1,70 e desvio padrão de 0,1. Com estas informações obtenha o seguinte conjunto de probabilidades:

# > A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

# > B. probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    

# > C. probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.


import pandas as pd
import numpy as np
from scipy.stats import norm

# Tabela padronizada
tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)


# Variável padronizada Z
media = 1.7

desv_padrao = 0.1

a = 1.8

z = (a - media) / desv_padrao
# 1.0000000000000009

probabilidade = norm.cdf(z)
# 0.8413447460685431
# A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros é de 84,13%

print(probabilidade)
