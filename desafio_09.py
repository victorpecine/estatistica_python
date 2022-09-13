# Em um lote de 10.000 latas de refrigerante foi realizada uma amostra aleatória simples de 100 latas e foi obtido o desvio padrão amostral do conteúdo das latas igual a 12 ml. O fabricante estipula um erro máximo sobre a média populacional de apenas 5 ml. Para garantir um nível de confiança de 95% qual o tamanho de amostra deve ser selecionado para este estudo?


# Cálculo para população finita
from scipy.stats import norm

populacao = 10000

desv_padrao = 12

e = 5

nivel_confianca = 0.95

area_dist_normal = (nivel_confianca / 2) + 0.5
# 0.975

z = norm.ppf(area_dist_normal)
# 1.959963984540054

# Tamanho da amostragem
n = ((z**2) * (desv_padrao**2) * (populacao)) / (((z**2) * (desv_padrao**2)) + ((e**2) * (populacao - 1)))
n = int(n.round())
# 22 latas
