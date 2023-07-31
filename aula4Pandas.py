#Biblioteca Pandas
import pandas as pd
from datetime import date
from datetime import datetime as dt


#Criando Series

pd.Series(data=5)

lista_nomes = 'Diego Ana Julia Mariana Maria'.split()

pd.Series(lista_nomes) #Cria uma Series com o valor a lista_nomes = 'Diego Ana Julia Mariana Maria'.split()

dados = {
    'nome1' : 'Diego',
    'nome2' : 'Ana',
    'nome3' : 'Julia',
    'nome4' : 'Mariana',
    'nome5' : 'Maria',
}

pd.Series(dados) # Cria uma Series com um dicionario

#Manipulaçao

series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print('Quantidade de linhas = ', series_dados.shape) #Retorna uma tupla com o número de linhas
print('Tipo de dados', series_dados.dtypes) #Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', series_dados.is_unique) #Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', series_dados.hasnans) #Verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count()) #Conta quantos valores existem (excluí os nulos)
print('Qual é o menor valor?', series_dados.min()) #Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) #Extrai o valor maximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados.mean()) #Extrai a média aritmética de uma Series numeria
print('Qual o desvio padrão', series_dados.std()) #Extrai o desvio padrão de uma séries numerica
print('Qual a mediana?', series_dados.median()) #Extrai a mediana de uma series numerica
print('\nResumo:\n', series_dados.describe()) #Exibe um resumo sobre os dados na Series

#DataFrame

lista_nomes2 = 'Diego Giovana Carol Julia Marta'.split()

dfs = pd.DataFrame(lista_nomes2, columns=['nome'])

print('\n')
print(pd.DataFrame(lista_nomes2, columns=['nome']))

data_extracao = date.today()
dfs['data_extracao'] = data_extracao
dfs['data_extracao'] = dfs['data_extracao'].astype('datetime64[ns]')
dfs=dfs.append({'nome' : 'TESTE', 'data_extracao' : dt(2020, 5, 17)}, ignore_index=True)
dfs.sort_values(by='data_extracao', ascending=False, inplace=True)

print(dfs.info())
dfs.head()

#Leitura de dados extruturados através de métodos

url = 'https://en.wikipedia.org/wiki/Minnesota'

dfs = pd.read_html(url)
print('\n')
print(type(dfs))
print(len(dfs))

#Filtros com testes booleanos
dfs = pd.DataFrame(lista_nomes, columns=['nome'])

data_extracao = dt.now
dfs['idade'] = 30
dfs=dfs.append({'nome' : 'TESTE', 'idade' : 25}, ignore_index=True)

print(dfs)
print(dfs.loc(dfs['idade'] < 30))

#Matplotlib, usado para criar graficos visuais
import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2) # pyplot gerencia a figura e o eixo

plt.show()

#Seaborn, cria graficos mais elaborados
import seaborn as sns