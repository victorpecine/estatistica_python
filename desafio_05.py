# Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal de desvio padrão populacional igual a 150 g. Selecionada uma amostra aleatório de 20 sacos de um lote específico, obteve-se um peso médio de 5.050 g. Construa um intervalo de confiança para a média populacional assumindo um nível de significância de 5%.


from tkinter import Scale
from scipy.stats import norm
import numpy as np

area_dist_normal = 0.5 + (0.95 / 2)

z = round(norm.ppf(area_dist_normal), 2)
# 1.96

media_amostral = 5050

nivel_significancia = 0.05

nivel_confianca = 1 - nivel_significancia
 
desv_padrao = 150

n = 20

raiz_n = round(np.sqrt(n), 2)
# 4.47

desv_padrao_medias_amostrais = round(desv_padrao / raiz_n, 2)
# 33.54 gramas

erro_inferencial = round(z * desv_padrao_medias_amostrais, 2)
# 65.74 gramas


# Intervalo de confiança para a média
intervalo = norm.interval(alpha=nivel_confianca, loc=media_amostral, scale=desv_padrao_medias_amostrais)

intervalo = ([round(x,2) if isinstance(x, float) else x for x in intervalo]) # Arredonda a tupla 'intervalo' para duas casas decimais

print(intervalo)
# [4984.22, 5115.78]
