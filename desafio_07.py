# Uma amostra aleatória simples de 1976 itens de uma população normalmente distribuída, com desvio padrão populacional igual a 11, resultou em uma média amostral de 28.

# Qual o intervalo de confiança de 90% para a média populacional?


from scipy.stats import norm
import numpy as np

n = 1976

desv_padrao = 11

media_amostral = 28

nivel_confianca = 0.90

area_dist_normal = 0.5 + (nivel_confianca / 2)
# 0.95

z = norm.ppf(area_dist_normal)
# 1.6448536269514722

raiz_n = np.sqrt(n)
# 44.45222154178574

desv_padrao_medias_amostrais = desv_padrao / raiz_n
# 0.24745669886621613

intervalo = norm.interval(alpha=nivel_confianca, loc=media_amostral, scale=desv_padrao_medias_amostrais)
# (27.592969951356466, 28.407030048643534)
