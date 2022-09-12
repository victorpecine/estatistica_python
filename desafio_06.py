# Para estimar o valor médio gasto por cada cliente de uma grande rede de fast-food, foi selecionada uma amostra de 50 clientes.

# Assumindo que o valor do desvio padrão da população seja de R$ 6,00 e que esta população se distribui normalmente, obtenha a margem de erro desta estimativa para um nível de confiança de 95%.


from scipy.stats import norm
import numpy as np

area_dist_normal = 0.5 + (0.95 / 2)
# 0.975

z = round(norm.ppf(area_dist_normal), 2)

n = 50

desv_padrao = 6

nivel_confianca = 0.95

raiz_n = round(np.sqrt(n), 2)
# 7.07

desv_padrao_medias_amostrais = round(desv_padrao / raiz_n, 2)
# R$ 0.85

erro_inferencial = round(z * desv_padrao_medias_amostrais, 2)
# R$ 1.67
