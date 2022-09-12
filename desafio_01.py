# Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de múltipla escolha com 3 alternativas possíveis em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova vale 10 pontos e a nota de corte seja 5, obtenha a probabilidade deste candidato acertar 5 questões e também a probabilidade deste candidato passar para a próxima etapa do processo seletivo.


from scipy.stats import binom

n = 10 # Número de questões

numero_alternativas_questao = 3

p = 1 / numero_alternativas_questao # Probabilidade de acerto

q = 1 - p # Probabilidade de erro

k = 5 # Total de eventos com sucesso (nota de corte)

# Probabilidade de acertar 5 questões
probabilidade_cinco_acertos = binom.pmf(k, n, p)
# 0.1365645480871816

# Soma das probabilidades de 5 a 10 questões certas
probabilidade_passar = binom.sf(4, n, p)
# 0.21312808006909525

# Soma das probabilidades de 0 a 4 questões certas
probabilidade_quatro_acertos =  binom.cdf(4, n, p)
# 0.7868719199309048
