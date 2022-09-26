# Fonte do dataset: https://www.kaggle.com/datasets/dongeorge/beer-consumption-sao-paulo


import pandas as pd


df_consumo = pd.read_csv('dados/consumo_cerveja.csv', sep=';')

# Tabela de estatísticas descritivas
estats_descits = df_consumo.describe()
#        temp_media    temp_min    temp_max       chuva         fds       consumo
# count  365.000000  365.000000  365.000000  365.000000  365.000000    365.000000
# mean    21.226356   17.461370   26.611507    5.196712    0.284932  25401.367123
# std      3.180108    2.826185    4.317366   12.417844    0.452001   4399.142703
# min     12.900000   10.600000   14.500000    0.000000    0.000000  14343.000000
# 25%     19.020000   15.300000   23.800000    0.000000    0.000000  22008.000000
# 50%     21.380000   17.900000   26.900000    0.000000    0.000000  24867.000000
# 75%     23.280000   19.600000   29.400000    3.200000    1.000000  28631.000000
# max     28.860000   24.500000   36.500000   94.800000    1.000000  37937.000000


# Matriz de correlação (método de Pearson)
correlacao = df_consumo.corr()

print(correlacao)
