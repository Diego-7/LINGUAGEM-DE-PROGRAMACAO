#tipos de variaveis
x = 10
nome = "Diego"
nota = 8.5
flag = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(flag))

#pedir nome e imprimir mensagem personalizada
nome = input("Digite um nome: ")
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello word" % (nome))

#extrutura condicional
qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

    #estrutura de decisão
    numero = 1

    while numero != 0:
        numero = int(input("Digite um número: "))

        if numero % 2 == 0:
            print("Número par!")
        else:
            print("Número ímpar!")

            #for
            nome1 = "Ana"

            for c in nome1: 
                print(c)

                #Função enumerate()
                nome2 = "Julia"
                for i, c in enumerate(nome2):
                    print(f"Posição = {i}, valor = {c}")

                    #Controles de repetição
                    for x in range(5):
                        print(x)

                        #Exemplo do uso do break
                        disciplina = "Linguagem de programação"

                        for c in disciplina:
                            if c == 'a':
                                break
                            else:
                                print(c)

                                #Exemplo de uso do continue
                                disciplina2 = "Linguagem de programação"
                                for c in disciplina2:
                                    if c == 'a':
                                        continue
                                    else:
                                        print(c)