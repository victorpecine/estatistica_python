from pyexpat import model
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn import metrics


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

# valores_imoveis_boxplot.savefig('graficos/valores_imoveis_boxplot.png')


# Distribuição de frequência
valores_dist_freq = sns.displot(data=df_imoveis['valor'])

valores_dist_freq.figure.set_size_inches(22,6)

valores_dist_freq.fig.suptitle('Distribuição de frequência\nValor dos imóveis', fontsize=18, y=1.10)

valores_dist_freq.set_xlabels('Valor em milhões de reais', fontsize=14)

valores_dist_freq.set_ylabels('Ocorrências', fontsize=14)

# valores_dist_freq.savefig('graficos/valores_imoveis_dist_freq.png')


# Dispersão entre as variáveis
sns.set_palette('Dark2')

disper_variaveis = sns.pairplot(data=df_imoveis, y_vars='valor', x_vars=['area', 'dist_praia', 'dist_farmacia'], height=5, kind='reg')

disper_variaveis.fig.suptitle('Disperção entre as variáveis', fontsize=12)

# disper_variaveis.savefig('graficos/imoveis_disper_entre_variaveis')


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

# valores_nova_dist_freq.savefig('graficos/valores_imoveis_nova_dist_freq.png')


# Nova dispersão entre as variáveis
nova_disper_variaveis = sns.pairplot(data=df_imoveis, y_vars='log_valor', x_vars=['log_area', 'log_dist_praia', 'log_dist_farmacia'], height=5, kind='reg')

nova_disper_variaveis.fig.suptitle('Nova disperção entre as variáveis', fontsize=12)

# nova_disper_variaveis.savefig('graficos/imoveis_nova_disper_entre_variaveis')


# Datasets de teste e treino

# Series da variável dependente
y = df_imoveis['log_valor']

X = df_imoveis[['log_area', 'log_dist_praia', 'log_dist_farmacia']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1240)
# 20% dos dados para teste
# 80% dos dados para treino


# Modelo log-linear
# Dataframe com constante
X_train_com_constante = sm.add_constant(X_train)

modelo_stats_models = sm.OLS(y_train, X_train_com_constante, hasconst=True).fit()
# OLS - método de estimação - Mínimos Quadrados Ordinários

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:              log_valor   R-squared:                       0.803
# Model:                            OLS   Adj. R-squared:                  0.803
# Method:                 Least Squares   F-statistic:                     5431.
# Date:                Thu, 29 Sep 2022   Prob (F-statistic):               0.00
# Time:                        15:17:57   Log-Likelihood:                -2002.9
# No. Observations:                4000   AIC:                             4014.
# Df Residuals:                    3996   BIC:                             4039.
# Df Model:                           3
# Covariance Type:            nonrobust
# =====================================================================================
#                         coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------
# const                 9.4002      0.061    155.300      0.000       9.282       9.519
# log_area              1.0460      0.012     88.088      0.000       1.023       1.069
# log_dist_praia       -0.4903      0.009    -56.832      0.000      -0.507      -0.473
# log_dist_farmacia    -0.0255      0.032     -0.808      0.419      -0.088       0.036
# ==============================================================================
# Omnibus:                       64.329   Durbin-Watson:                   2.026
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              111.270
# Skew:                           0.113   Prob(JB):                     6.89e-25
# Kurtosis:                       3.785   Cond. No.                         48.2
# ==============================================================================

# O p_valor de log_dist_farmaciaé muito maior que a significância 0.05, demonstrando que essa variável é estatisticamente insignificante e pode ser removida do modelo
# A Prob (F-statistic) <= 0.05 permite aceitar a hipótese nula: o ajuste do modelo somente com o intercepto e seu modelo são iguais


# Novo modelo de treino e teste sem a variável log_dist_farmacia
X = df_imoveis[['log_area', 'log_dist_praia']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1240)

X_train_com_constante = sm.add_constant(X_train)

modelo_stats_models = sm.OLS(y_train, X_train_com_constante, hasconst=True).fit()

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:              log_valor   R-squared:                       0.803
# Model:                            OLS   Adj. R-squared:                  0.803
# Method:                 Least Squares   F-statistic:                     8147.
# Date:                Thu, 29 Sep 2022   Prob (F-statistic):               0.00
# Time:                        16:03:49   Log-Likelihood:                -2003.2
# No. Observations:                4000   AIC:                             4012.
# Df Residuals:                    3997   BIC:                             4031.
# Df Model:                           2
# Covariance Type:            nonrobust
# ==================================================================================
#                      coef    std err          t      P>|t|      [0.025      0.975]
# ----------------------------------------------------------------------------------
# const              9.3896      0.059    158.972      0.000       9.274       9.505
# log_area           1.0462      0.012     88.130      0.000       1.023       1.069
# log_dist_praia    -0.4904      0.009    -56.851      0.000      -0.507      -0.474
# ==============================================================================
# Omnibus:                       64.732   Durbin-Watson:                   2.027
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              112.194
# Skew:                           0.113   Prob(JB):                     4.34e-25
# Kurtosis:                       3.789   Cond. No.                         46.6
# ==============================================================================

# Prob (F-statistic): <= 0.05 -> modelo aceito
# p_valor <= 0.05 -> modelo aceito


# Previsão de valores
modelo_com_dados_treino = LinearRegression().fit(X_train, y_train)

r_quadrado_dados_treino = modelo_com_dados_treino.score(X_train, y_train)
# 0.8030177259167965

# Previsão para os dados de teste
y_previsto = modelo_com_dados_treino.predict(X_test)

r_quadrado_dados_teste = metrics.r2_score(y_test, y_previsto)
# 0.7995385786900894


# Previsão pontual com dados de teste
entrada = X_test[0:1]
#       log_area  log_dist_praia
# 2479  4.382027        0.523941

log_valor_pontual_previsto = modelo_com_dados_treino.predict(entrada)[0]
# 13.717087608555264

valor_pontual_previsto = np.exp(log_valor_pontual_previsto)
# R$ 906265.5182179569


# Simulador simples
def simulador(area, dist_praia):
    entrada_log = [[np.log(area), np.log(dist_praia) + 1]]
    y_previsto_simulador = np.exp(modelo_com_dados_treino.predict(entrada_log)[0])

    return y_previsto_simulador

print(simulador(250, 1))
# 2363600.3627711697
