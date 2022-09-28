import pickle
from ipywidgets import widgets, HBox, VBox
from IPython.display import display


modelo_salvo = open('modelos/modelo_consumo_temp_max_chuva_fds','rb') # rb = read binary

modelo = pickle.load(modelo_salvo)

modelo_salvo.close()


temp_max = 16

chuva = 12.2

fds = 0

# variaveis = [[temp_max, chuva, fds]]

# previsao = modelo.predict(variaveis)
# 16589.40810411 litros


# Simulador interativo
# Criando os controles do formulário
temp_max = widgets.Text(description='Temperatura máxima (°C)')
chuva = widgets.Text(description='Chuva (ml)')
fds = widgets.Text(description='Final de semana?')

botao = widgets.Button(description='Simular')

# Posicionando os controles
left = VBox([temp_max, chuva, fds])
inputs = HBox([left])

# Função de simulação
def simulador(sender):
    entrada=[[
                float(temp_max.value if temp_max.value else 0), 
                float(chuva.value if chuva.value else 0),
                float(fds.value if fds.value else 0), 
             ]]
    print('$ {0:.2f}'.format(modelo.predict(entrada)[0]))

# Atribuindo a função 'simulador' ao evento click do botão
botao.on_click(simulador)

display(inputs, botao)
