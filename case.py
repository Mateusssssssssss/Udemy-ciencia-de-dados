import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
#Abrir arquivo
dataset = pd.read_csv('case_estagio.csv')
#verificar se a null em alguma coluna.
null_data = dataset.isnull().sum()
# Descreve media. mediana. min e maximo, total de linhas.
dataset_describe = dataset['price'].describe()
print(dataset_describe)
#Preenchendo valores nulos na coluna 'product_category_name' com 'Outros
dataset.fillna('Outros', inplace=True)
#agrupar por categoria
agrupar_category = dataset.groupby(['product_category_name']).size()
#forma eficaz de visualizar a distribuição de um 
# conjunto de dados e identificar outliers.
#outliers indicam valores extremamente altos ou baixos 
#em relação à distribuição dos dados.
sb.boxplot(dataset['price']).set_title('Preços')
plt.show()
#Histograma dos preços para visualizar a distribuição dos valores e 
#identificar possíveis valores exorbitantes.
sb.displot(dataset['price'])
plt.show()
#soma de price por category
agrupar_category_price = dataset.groupby(['product_category_name'])['price'].sum()
#grafico de barras cor azul / Sales por categoria
agrupar_category.plot.bar(color='blue')
#Adiciona um titulo ao grafico
plt.title('Número de Vendas por Categoria')
#cria o grafico vendas por category
plt.show()
#Soma do preço de vendas por Category
agrupar_category_price.plot.bar(color='red')
#Cria o grafico soma de preço por category
plt.title('Valores de vendas por Categoria')
plt.show()
dataset.to_csv('clean_case')
