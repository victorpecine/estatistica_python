# Estamos estudando o rendimento mensal dos chefes de domicílios com renda até R$ 5.000,00 no Brasil. Nosso supervisor determinou que o erro máximo em relação a média seja de R$ 10,00. Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$ 1.082,79. Para um nível de confiança de 95% qual deve ser o tamanho da amostra de nosso estudo?

# Cálculo para população infinita
from scipy.stats import norm

a = 5000

e = 10

desv_padrao = 1082.79

nivel_confianca = 0.95

area_dist_normal = (nivel_confianca / 2) + 0.5
# 0.975

z = norm.ppf(area_dist_normal)
# 1.959963984540054

n = (z * (desv_padrao / e))**2 # Tamanho da amostra
n = int(n.round())
# 45039
