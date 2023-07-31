#Listas
frutas = ['maça', 'uva', 'amora', 'morango', 'pessego']
carros = ['gol', 'uno', 'corsa', 'celta', 'nivus', 'civic']

#Tuplas
armas = ('revolver', 'fuzil', 'escopeta', 'espingarda')

#Extrutura de repetição sequencial
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')

#gerar lista
numeros = list(range(0,21))

print(numeros)

#gerar tupla

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

#Exercicio 1
texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""

print(f"Tamanho do texto = {len(texto)}")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
lista_palavras = texto.split()
print(f"Tamanho da lista de palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")

print(f"Quantidade de vezes que string ou strings aparecem = {total}")

#extrutura de dados

#dicionarios
dicionario1 = {}
dicionario2 = {'one':1, 'two':2, 'three':3}
dict()

#Exemplo 1 - Criação de dicionario vazio, com a tribuição posterior de chave valor
dici_1 = {}
dici_1['nome'] = "Diego"
dici_1['idade'] = 25

#Exemplo 2 - Criação de dicionario usando um par de elementos na forma chave:valor
dici_2 = {'nome':'Ana', 'idade':18}

#Exemplo 3 - Criação de dicionario com uma lista de tuplas. Cada tupla representa um par chave:valor
dici_3 = dict([('nome', "Carol"), ('idade',22)])

#Objetos do tipo array NumPy

#Exemplo
import numpy

matriz_1_1 = numpy.array([1,2,3]) #Cria matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1, 2], [3, 4]]) #Cria matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) #Cria matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) #Cria matriz 2 linhas e 3 colunas

print(type(matriz_1_1))
print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_1_1 = \n', matriz_3_2)
print('\n matriz_1_1 = \n', matriz_2_3)

#Busca binária

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        #Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        #Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True #Se o valor for encontrado para aqui
        
        return False #Se chegar até aqui, significa que o valor não foi encontrado 
    
    #Algoritmos de Ordenação

    #Exemplo 1  
    lista2 = [10, 4, 1, 15, -3]

    lista_ordenada1 = sorted(lista2)

    lista_ordenada2 = lista2.sort()

    print('lista = ', lista2, '\n')

    print('lista_ordenada1 = ', lista_ordenada1)
    print('lista_ordenada2 = ', lista_ordenada2)

    print('lista = ', lista2)

    #Exemplo 2

    lista3 = [7, 4]

    if lista3[0] > lista3[1]:
        aux = lista3[1]
        lista3[1]
        lista3[0] = aux

    print(lista3)
    

 #Exemplo 3

def executar_selection_sort(lista4):
        n = len(lista4)
        for i in range(0, n):
            index_menor = i
            for j in range (i+1, n):
                if lista4[j] < lista4[index_menor]:
                    index_menor = j
                lista4[i], lista4[index_menor] = lista4[index_menor], lista4[i]
            return lista4

lista4 = [10, 9, 5, 8, 11, 3]
print(executar_selection_sort(lista4))


