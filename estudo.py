import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
#Abrir arquivo
dataset = pd.read_csv('case_estagio.csv')
#verificar se a null em alguma coluna.
null_data = dataset.isnull().sum()
#indetificado que havia null na coluna Product_category_name, 
#null bustituido por Outros
dataset.fillna('Outros', inplace=True)
#agrupar por categoria
agrupar = dataset.groupby(['product_category_name']).size()
print(agrupar)
#grafico de barras cor azul
agrupar.plot.bar('blue')
#Cria o grafico
plt.show()