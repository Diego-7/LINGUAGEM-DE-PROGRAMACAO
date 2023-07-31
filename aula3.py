#Minha primeira classe em Python

import sqlite3


class PrimeiraClasse:

    def imprimir_mensagem(self, nome): #Criando um método
        print(f"Olá {nome}, seja bem vindo(a)!")
        objeto1 = PrimeiraClasse() #Instanciando um objeto do tipo PrimeiraClasse
        objeto1.imprimir_mensagem('Ana') #Invocando método

        class Televisao:
            def __init__(self):
                self.volume = 10
            def aumentar_volume(self):
                self.volume += 1
            def diminuir_volume(self):
                self.volume -= 1

                tv = Televisao()
                print("Volume ao ligar a tv = ", tv.volume)
                tv.aumentar_volume()
                print("Volume atual = ", tv.volume)

            class ContaCorrente:
                    def __init__(self):
                        self._saldo = None
                    def depositar(self, valor):
                        self._saldo += valor
                    def consultar_saldo(self):
                        return self._saldo
                    
    #Herança

    class Pessoa:
        def __init__(self):
            self.cpf = None
            self.nome = None
            self.endereco = None

    # class Funcionario(Pessoa):
      #  def __init__(self):
       #     self.matricula = None
        #    self.salario = None
        #def bater_ponto(self):
            #codigo aqui
         #   pass
        #def fazer_login(self):
            #codigo aqui
         #   pass

       # f1 = Funcionario()
      #  f1.nome = "Funcionario A"
      #  print(f1.nome)

       #c1 = Cliente()
       # c1.cpf = "111.111.111-11"
        #print(c1.cpf) */

    #Linguagem de consulta SQL

    import sqlite3

# Cria banco de cados
conn = sqlite3.connect('aulaDB.db')
print(type(conn))

#Criando a tabela

ddl_create = """
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT, 
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);
"""

cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))

print("Tabela criada!")
print("Descrisão do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
""")

conn.commit()

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),
    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)""", dados)

conn.commit()

print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()

print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor = 5")
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conn.close()
[(5, 'Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01')]

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()

cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")
print('Tabelas:')
for tabela in cursor.fetchall():
    print(tabela)

# Captura a DDL usada para criar a tabela
tabela = 'fornecedor'
cursor.execute(f"""SELECT sql FROM sqlite_master WHERE type='table' AND name='{tabela}'""")
print(f'\nDDL da tabela {tabela}:')
for schema in cursor.fetchall():
    print("%s" % (schema))
    
cursor.close()
conn.close()