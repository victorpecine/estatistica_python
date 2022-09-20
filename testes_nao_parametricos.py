# Antes de cada partida do campeonato nacional de futebol, as moedas utilizadas pelos árbitros devem ser verificadas para se ter certeza de que não são viciadas, ou seja, que não tendam para determinado resultado. Para isso um teste simples deve ser realizado antes de cada partida. Este teste consiste em lançar a moeda do jogo 50 vezes e contar as frequências de CARAS e COROAS obtidas. A tabela abaixo mostra o resultado obtido no experimento:

#             |CARA|COROA|
# |Observado  | 17 | 33  |
# |Esperado   | 25 | 25  |

# A um nível de significância de 5%, é possível afirmar que a moeda não é honesta, isto é, que a moeda apresenta uma probabilidade maior de cair com a face CARA voltada para cima?


import pandas as pd
from scipy.stats import chi, chisquare


tabela_t_chi_2 = pd.DataFrame(
    [], 
    index=[i for i in range(1, 31)],
    columns = [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.975, 0.95, 0.99, 0.995]
)

for index in tabela_t_chi_2.index:
    for column in tabela_t_chi_2.columns:
        tabela_t_chi_2.loc[index, column] = "{0:0.4f}".format(chi.ppf(float(column), index)**2)

tabela_t_chi_2.index.name='Graus de Liberdade'
tabela_t_chi_2.rename_axis(['p'], axis=1, inplace = True)



freq_observada = [17, 33]

freq_esperada = [25, 25]

significancia = 0.05

confianca = 1 - significancia

k = 2 # Número de eventos possíveis

graus_de_liberdade = k - 1


# Hipóteses
# H0 -> freq_cara = freq_coroa
# H1 -> freq_cara != freq_coroa

qui_quadrado_alpha = chi.ppf(confianca, graus_de_liberdade) ** 2
# 3.8414588206941245


# Cálculo da estatística-teste e verificação desse valor com as áreas de aceitação e rejeição do teste
qui_quadrado, p_valor = chisquare(f_obs=freq_observada, f_exp=freq_esperada)
# qui_quadrado = 5.12
# p_valor = 0.023651616655356


# Valor crítico qui
if qui_quadrado >= qui_quadrado_alpha:
    print('Hipótese nula H0 rejeitada pelo valor crítico qui\nA moeda utilizada não é honesta e deve ser trocada')
else:
    print('Hipótese nula H0 aceita pelo valor crítico qui\nA moeda utilizada é honesta e não precisa ser trocada')

# Hipótese nula H0 rejeitada pelo valor crítico qui
# A moeda utilizada não é honesta e deve ser trocada


# Valor p
if p_valor <= significancia:
    print('Hipótese nula H0 rejeitada pelo valor p\nA moeda utilizada não é honesta e deve ser trocada')
else:
    print('Hipótese nula H0 aceita pelo valor p\nA moeda utilizada é honesta e não precisa ser trocada')

# Hipótese nula H0 rejeitada pelo valor p
# A moeda utilizada não é honesta e deve ser trocada
