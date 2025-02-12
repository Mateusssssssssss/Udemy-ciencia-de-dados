from statistics import *
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

#ler o data set
dataset = pd.read_csv('tempo.csv')
#descreve o dataset
data_describe = dataset.describe()
#boxplot com outlier em 1220
sb.boxplot(dataset['Temperatura'])
plt.show()
#ler a Tabela temperatuda do dataset
data_temp = dataset['Temperatura']
#moda da temperatura
moda_temp_s = mode(dataset['Temperatura'])
#Onde havia outlier 1220, substituido pelo valor da moda
dataset.loc[dataset['Temperatura'] == 1220, 'Temperatura'] = moda_temp_s
#boxplot depois do ajuste
sb.boxplot(dataset['Temperatura'])
plt.show()
#verificar se a valores nulls
null_data = dataset['Umidade'].isnull().sum()
#Boxplot para possivel outlier
sb.boxplot(dataset['Umidade'])
plt.show()
#calcula a moda da coluna umidade
colunm_umidade = mode(dataset['Umidade'])
#subtitui o valor null na coluna umidade para a moda
dataset['Umidade'].fillna(colunm_umidade, inplace=True)
#identificado outlier a 200, logo nao existiria, codigo altera esse valor
#por o valor mais frequente
dataset.loc[dataset['Umidade'] == 200, 'Umidade'] = colunm_umidade
#Procura de valores nulos
null_vento = dataset['Vento'].isnull().sum()
#Calculo da moda coluna vento
colunm_vento = mode(dataset['Vento'])
#substituido o valor Null da tabela Pela moda.
dataset['Vento'].fillna(colunm_vento, inplace=True)

print(dataset)
#salva o arquivo Limpo
dataset.to_csv('Tempo_clean.csv', index=False)


