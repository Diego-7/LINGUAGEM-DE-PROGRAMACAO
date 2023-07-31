import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2) # pyplot gerencia a figura e o eixo

plt.show()

#Figura com eixo como variavel
import numpy as np

x = range(5)
x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.

fig, ax = plt.subplots(1, 2, figsize=(12, 5)) # Cria figura com subplots: 1 linha, 2 colunas e eixos

print("Tipo de ax = ", type(ax))
print("Conteúdo de ax[0] = ", ax[0])
print("Conteúdo de ax[1] = ", ax[1])

ax[0].plot(x, x, label='eq_1') # cria gráfico sobre eixo 0
ax[0].plot(x, x**2, label='eq_2') # cria gráfico sobre eixo 0
ax[0].plot(x, x**3, label='eq_3') # cria gráfico sobre eixo 0
ax[0].set_xlabel('Eixo x')
ax[0].set_ylabel('Eixo y')
ax[0].set_title("Gráfico 1")
ax[0].legend()

ax[1].plot(x, x, 'r--', label='eq_1') # cria gráfico sobre eixo 1
ax[1].plot(x**2, x, 'b--', label='eq_2') # cria gráfico sobre eixo 1
ax[1].plot(x**3, x, 'g--', label='eq_3') # cria gráfico sobre eixo 1
ax[1].set_xlabel('Novo Eixo x')
ax[1].set_ylabel('Novo Eixo y')
ax[1].set_title("Gráfico 2")
ax[1].legend()

plt.show()

#Figura sem eixo como variavel
x = range(5)
x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.

fig = plt.subplots(figsize=(12, 5)) # Cria figura sem eixo
plt.subplot(121) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 1           
plt.plot(x, x, label='eq_1')
plt.plot(x, x**2, label='eq_2')
plt.plot(x, x**3, label='eq_3')
plt.title("Gráfico 1")
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()

plt.subplot(122) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 2            
plt.plot(x, x, 'r--', label='eq_1')
plt.plot(x**2, x, 'b--', label='eq_2')
plt.plot(x**3, x, 'g--', label='eq_3')
plt.title("Gráfico 2")
plt.xlabel('Novo eixo x')
plt.ylabel('Novo eixo y')
plt.legend()

plt.show()

#Biblioteca Pandas criando DataFrame
import pandas as pd

dados = {
    'turma':['A', 'B', 'C'],
    'qtde_alunos':[33, 50, 45]
}
df=pd.DataFrame(dados)

print(df)

#Criando grafico
df.plot(x='turma', y='qtde_alunos', kind='bar')
df.plot(x='turma', y='qtde_alunos', kind='barh')
df.plot(x='turma', y='qtde_alunos', kind='line')

#grafico de pizza
df.set_index('turma').plot(y='qtde_alunos', kind='pie')

plt.show()

#Biblioteca Seaborn
import seaborn as sns

sns.set(style="whitegrid") # opções: darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset('tips')

print(df_tips.info())

#comparação gastos homens e mulheres
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)

plt.show()

#valor medio diario de vendas
plt.figure(figsize=(10, 5))

ax = sns.barplot(x="day", y="total_bill", data=df_tips)

ax.axes.set_title("Venda média diária", fontsize=14)
ax.set_xlabel("Dia", fontsize=14)
ax.set_ylabel("Venda média ", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()

#FUNÇÃO COUNTPLOT()
plt.figure(figsize=(10, 5))
sns.countplot(data=df_tips, x="day")
plt.show()

#Parametro hue
plt.figure(figsize=(10, 5))
sns.countplot(data=df_tips, x="day", hue="sex")
plt.show()

#FUNÇÃO SCARTTERPLOT()
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_tips, x="total_bill", y="tip")
plt.show()







