# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma distribuição aproximadamente normal, com média 1,70 e desvio padrão de 0,1. Com estas informações obtenha o seguinte conjunto de probabilidades:

# > A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

# > B. probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    

# > C. probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.


import pandas as pd
import numpy as np
from scipy.stats import norm

# Variável padronizada Z
media = 1.7

desv_padrao = 0.1

a = 1.9

z = (a - media) / desv_padrao
# 1.0000000000000009

probabilidade = norm.sf(z)
# 0.8413447460685431
# A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros é de 84,13%

print(z)
print(probabilidade)

# a_inferior = 1.6

# z_inferior = (a_inferior - media) / desv_padrao
# # -0.9999999999999987

# probabilidade_inferior = norm.cdf(z_inferior)
# # 0.1586552539314574

# probabilidade = norm.cdf(z_superior) - norm.cdf(z_inferior)
# # 0.6826894921370857
# # B. probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros é de 68,26%
