import pickle


modelo_salvo = open('modelos/modelo_consumo_temp_max_chuva_fds','rb') # rb = read binary

modelo = pickle.load(modelo_salvo)

modelo_salvo.close()


temp_max = 16

chuva = 12.2

fds = 0

variaveis = [[temp_max, chuva, fds]]

previsao = modelo.predict(variaveis)
# 16589.40810411 litros
