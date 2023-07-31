#Taxa selic no decorrer do tempo

import pandas as pd

#Importar base de dados
df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

#Remover linhas duplicadas
df_selic.drop_duplicates(keep='last', inplace=True)

#Criar novas colunas
from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = 'Autor'

df_selic.head()

#Método to_datetime() e astype()
df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')

#Series.str
df_selic['responsavel'] = df_selic['responsavel'].str.upper()

#Método sort_values()
df_selic.sort_values(by='data', ascending=False, inplace=True)

#Método reset_index e set_index()
df_selic.reset_index(drop=True, inplace=True)

lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]

df_selic.set_index(keys=[lista_novo_indice], inplace=True)

#indice maior e indice menor
df_selic['valor'].idxmin()
df_selic['valor'].idxmax()

#Filtros com loc
df_selic.loc['selic_100']
df_selic.loc[['selic_0', 'selic_38', 'selic_94']]
df_selic.loc[:'selic_18']

#Loc com colunas
df_selic.loc[['selic_0', 'selic_38', 'selic_94']]['valor']
df_selic.loc[['selic_0', 'selic_38', 'selic_94']][['valor', 'data_extracao']]

df_selic.loc[['selic_0', 'selic_4', 'selic_200'], 'valor']
df_selic.loc[['selic_0', 'selic_38', 'selic_94'], ['valor', 'data_extracao']]

#iloc
df_selic.iloc[:5]

#Filtros com testes booleanos
teste = df_selic['valor'] < 0.01
#print(type(teste))
#print(teste[:5])

teste2 = df_selic['data'] >= pd.to_datetime('2020-01-01')
#print(type(teste2))
#print(teste2[:5])

#Em pandas & = and e | = or, combinando consultas
teste3 = (df_selic['valor'] < 0.01) & (df_selic['data'] >= pd.to_datetime('2020-01-01'))

teste4 = (df_selic['valor'] < 0.01) | (df_selic['data'] >= pd.to_datetime('2020-01-01'))

#Aplicando loc no dataframe
filtro1 = df_selic['valor'] < 0.01
df_selic.loc[filtro1]

data1 = pd.to_datetime('2020-01-01')
data2 = pd.to_datetime('2020-01-31')

filtro_janeiro_2020 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

df_janeiro_2020 = df_selic.loc[filtro_janeiro_2020]
df_janeiro_2020.head()

#novo filtro
data1 = pd.to_datetime('2019-01-01')
data2 = pd.to_datetime('2019-01-31')

filtro_janeiro_2019 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

df_janeiro_2019 = df_selic.loc[filtro_janeiro_2019]
df_janeiro_2019.head()

#Extraindo valores para analise de dados
print('Mínimo geral = ', df_selic['valor'].min())
print('Mínimo janeiro de 2019 = ', df_janeiro_2019['valor'].min())
print('Mínimo janeiro de 2020 = ',df_janeiro_2020['valor'].min(), '\n')

print('Máximo geral = ', df_selic['valor'].max())
print('Máximo janeiro de 2019 = ', df_janeiro_2019['valor'].max())
print('Máximo janeiro de 2020 = ',df_janeiro_2020['valor'].max(), '\n')

print('Média geral = ', df_selic['valor'].mean())
print('Média janeiro de 2019 = ', df_janeiro_2019['valor'].mean())
print('Média janeiro de 2020 = ',df_janeiro_2020['valor'].mean(), '\n')

#Salvar em csv  
#df_selic.to_csv('dados_selic.csv')

#Métodos para bancos de dados

#pd.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
#pd.read_sql_query(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)

#conectar com postgresql e mysql

#import psycopg2

#host = 'XXXXX'
#port = 'XXXXX'
#database = 'XXXXX'
#username = 'XXXXX'
#password = 'XXXXX'
#conn_str = fr"dbname='{database}' user='{username}' host='{host}' password='{password}' port='{port}'"
#conn = psycopg2.connect(conn_str)

#query = "select * from XXX.YYYY"
#df = pd.read_sql(query, conn)import mysql.connector

#host = 'XXXXX'
#port = 'XXXXX'
#database = 'XXXXX'
#username = 'XXXXX'
#password = 'XXXXX'

#conn_str = fr"host={host}, user={username}, passwd={password}, database={database}"
#conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")

#query = "select * from XXX.YYYY"
#df = pd.read_sql(query, conn)




