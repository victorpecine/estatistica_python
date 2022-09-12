# Um restaurante recebe em média 20 pedidos por hora. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?


from scipy.stats import poisson

media_pedidos = 20

k = 15 # Número de sucessos

probabiliade = poisson.pmf(k, media_pedidos)
# 0.05164885353175814
