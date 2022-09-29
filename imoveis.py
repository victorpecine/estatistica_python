import pandas as pd
import seaborn as sns
import numpy as np


sns.set_palette('OrRd')

df_imoveis = pd.read_csv('dados/imoveis.csv', sep=';')

df_imoveis.columns = df_imoveis.columns.str.lower() # Cabeçalho do dataframe minúsculo
# valor (R)$
# area (m^2)
# dist_praia (km)
# dist_farmacia (km)


# Estatísticas descritivas
estat_desc = df_imoveis.describe().round(2)
#              valor     area  dist_praia  dist_farmacia
# count      5000.00  5000.00     5000.00        5000.00
# mean    1402926.39   121.94        3.02           0.50
# std     1883268.85    90.54        3.17           0.29
# min       75000.00    16.00        0.00           0.00
# 25%      460000.00    70.00        0.44           0.24
# 50%      820000.00    93.00        1.48           0.50
# 75%     1590000.00   146.00        5.61           0.75
# max    25000000.00  2000.00       17.96           1.00


# Correlação
correlacao = df_imoveis.corr().round(4)
#                 valor    area  dist_praia  dist_farmacia
# valor          1.0000  0.7110     -0.3665        -0.0244
# area           0.7110  1.0000     -0.2834        -0.0310
# dist_praia    -0.3665 -0.2834      1.0000         0.0256
# dist_farmacia -0.0244 -0.0310      0.0256         1.0000


# Análises gráficas
# Boxplot
valores_boxplot = sns.boxplot(data=df_imoveis['valor'], orient='h', width=0.5)

valores_boxplot.figure.set_size_inches(22,6)

valores_boxplot.set_title('Preço dos imóveis', fontsize=18)

valores_boxplot.set_xlabel('R$', fontsize=12)

valores_imoveis_boxplot = valores_boxplot.get_figure()

valores_imoveis_boxplot.savefig('graficos/valores_imoveis_boxplot.png')


# Distribuição de frequência
valores_dist_freq = sns.displot(data=df_imoveis['valor'])

valores_dist_freq.figure.set_size_inches(22,6)

valores_dist_freq.fig.suptitle('Distribuição de frequência\nValor dos imóveis', fontsize=18, y=1.10)

valores_dist_freq.set_xlabels('Valor em milhões de reais', fontsize=14)

valores_dist_freq.set_ylabels('Ocorrências', fontsize=14)

valores_dist_freq.savefig('graficos/valores_imoveis_dist_freq.png')


# Dispersão entre as variáveis
sns.set_palette('Dark2')

disper_variaveis = sns.pairplot(data=df_imoveis, y_vars='valor', x_vars=['area', 'dist_praia', 'dist_farmacia'], height=5, kind='reg')

disper_variaveis.fig.suptitle('Disperção entre as variáveis', fontsize=12)

disper_variaveis.savefig('graficos/imoveis_disper_entre_variaveis')


# Transformação das variáveis para distribuição normal
df_imoveis['log_valor'] = np.log(df_imoveis['valor'])

df_imoveis['log_area'] = np.log(df_imoveis['area'])

df_imoveis['log_dist_praia'] = np.log(df_imoveis['dist_praia'] + 1)
# log(0) = -inf
# Para evitar erros foi somado 1
# Essa soma não altera a variação dos valores

df_imoveis['log_dist_farmacia'] = np.log(df_imoveis['dist_farmacia'] + 1)

# Nova distribuição de frequência
valores_nova_dist_freq = sns.displot(data=df_imoveis['log_valor'])

valores_nova_dist_freq.figure.set_size_inches(22,6)

valores_nova_dist_freq.fig.suptitle('Nova distribuição de frequência\nValor dos imóveis', fontsize=18, y=1.10)

valores_nova_dist_freq.set_xlabels('Log do valor', fontsize=14)

valores_nova_dist_freq.set_ylabels('Ocorrências', fontsize=14)

valores_nova_dist_freq.savefig('graficos/valores_imoveis_nova_dist_freq.png')
