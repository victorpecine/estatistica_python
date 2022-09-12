# Temos uma cidade do interior que realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. Na última, a proporção de participantes do sexo feminino foi de 60% e o total foi de 30 equipes com 12 integrantes cada uma.

# Com as informações acima, deveremos responder quantas equipes são formadas por 8 mulheres.


from scipy.stats import binom

p = 0.6 # Probabilidade de uma mulher ser escolhida

n = 12 # Número de integrantes

k = 8 # Quantidade de mulheres na equipe

# Probabilidade do time ter 8 mulheres
probabilidade = binom.pmf(k, n, p)
# 0.21284093952


# Média da distribuição binomial
total_equipes = 30
media_equipes_oito_mulheres = round(total_equipes * probabilidade)

print(media_equipes_oito_mulheres)