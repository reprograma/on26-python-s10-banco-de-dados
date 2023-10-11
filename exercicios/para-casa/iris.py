# Atividade para casa - semana 10

# Baixar um arquivo csv no 'kaggle' e criar com ele:
# select; insert into, update e delete


# Arquivo csv de espécies de íris - flor

# Após o código estão os exemplos de uso separadamente

import sqlite3
import csv

# Função para criar a tabela 'iris' se não existir
def criar_tabela(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS iris (
            id INTEGER PRIMARY KEY,
            sepal_length REAL,
            sepal_width REAL,
            petal_length REAL,
            petal_width REAL,
            species TEXT
        )
    ''')

# Função para inserir dados na tabela 'iris'
def inserir_dados(cursor, sepal_length, sepal_width, petal_length, petal_width, species):
    cursor.execute('INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (?, ?, ?, ?, ?)',
                   (sepal_length, sepal_width, petal_length, petal_width, species))

# Função para atualizar dados na tabela 'iris' com base no ID
def atualizar_dados(cursor, id_registro, sepal_length, sepal_width, petal_length, petal_width, species):
    cursor.execute('''
        UPDATE iris
        SET sepal_length = ?, sepal_width = ?, petal_length = ?, petal_width = ?, species = ?
        WHERE id = ?
    ''', (sepal_length, sepal_width, petal_length, petal_width, species, id_registro))

# Função para excluir um registro na tabela 'iris' com base no ID
def excluir_registro(cursor, id_registro):
    cursor.execute('DELETE FROM iris WHERE id = ?', (id_registro,))
 
 # excluir_registro(cursor, 2)


# # Função para realizar uma seleção (select) e retornar os registros
def selecionar_registros(cursor, limit=5):
    cursor.execute('SELECT * FROM iris LIMIT ?', (limit,))
    registros = cursor.fetchall()
    return registros

 # Conectar ao banco de dados SQLite ou criar um novo se não existir
banco = sqlite3.connect('iris.db')
cursor = banco.cursor()

# Criar a tabela 'iris'
criar_tabela(cursor)

# Abrir o arquivo CSV 'iris.csv' e inserir os dados na tabela
with open('iris.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    # Pule o cabeçalho
    next(leitor_csv)
    for linha in leitor_csv:
        # Ajuste o número de valores para corresponder ao número de colunas no arquivo CSV
        sepal_length, sepal_width, petal_length, petal_width, species, _ = linha
        inserir_dados(cursor, sepal_length, sepal_width, petal_length, petal_width, species)

# Para salvar as alterações no banco de dados
banco.commit()

# Realizar uma seleção (select) para verificar os dados inseridos
registros = selecionar_registros(cursor)
print("Primeiros 5 registros:")
for registro in registros:
    print(registro)

# Atualizar um registro
atualizar_dados(cursor, 1, 5.1, 3.5, 1.4, 0.2, 'Iris-setosa')

# Excluir um registro: id 2
excluir_registro(cursor, 2)

# Realizar uma seleção (select) novamente para verificar as alterações
registros = selecionar_registros(cursor)
print("\nApós atualização e exclusão:")
for registro in registros:
    print(registro)

# Fechar a conexão com o banco de dados
banco.close()

# DESCOMENTE ENTRE AS LINHAS 88 - 123  PARA EXECUTAR SOMENTE 'SELECT'

# import sqlite3

# # Função para criar a tabela 'iris' se não existir
# def criar_tabela(cursor):
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS iris (
#             id INTEGER PRIMARY KEY,
#             sepal_length REAL,
#             sepal_width REAL,
#             petal_length REAL,
#             petal_width REAL,
#             species TEXT
#         )
#     ''')

# # Função para realizar uma seleção (select) e retornar os registros
# def selecionar_primeiros_registros(cursor, limit=5):
#     cursor.execute('SELECT * FROM iris LIMIT ?', (limit,))
#     registros = cursor.fetchall()
#     return registros

# # Conectar ao banco de dados SQLite ou criar um novo se não existir
# banco = sqlite3.connect('iris.db')
# cursor = banco.cursor()

# # Criar a tabela 'iris'
# criar_tabela(cursor)

# # Realizar uma seleção (select) para verificar os 5 primeiros registros
# registros = selecionar_primeiros_registros(cursor)
# print("Primeiros 5 registros:")
# for registro in registros:
#     print(registro)

# # Fechar a conexão com o banco de dados
# banco.close()


# DESCOMENTE ENTRE AS LINHAS 128 - 157 PARA EXECUTAR 'ATUALIZAR'

# import sqlite3

# # Função para atualizar dados na tabela 'iris' com base no ID
# def atualizar_dados(cursor, id_registro, sepal_length, sepal_width, petal_length, petal_width, species):
#     cursor.execute('''
#         UPDATE iris
#         SET sepal_length = ?, sepal_width = ?, petal_length = ?, petal_width = ?, species = ?
#         WHERE id = ?
#     ''', (sepal_length, sepal_width, petal_length, petal_width, species, id_registro))

# # Conectar ao banco de dados SQLite
# banco = sqlite3.connect('iris.db')
# cursor = banco.cursor()

# # Realize a atualização desejada (neste caso, alterando o valor de "species" para "Iris-versicolor")
# atualizar_dados(cursor, id_registro=1, sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='Iris-versicolor')

# # Faça o commit para salvar as alterações no banco de dados
# banco.commit()

# # Realize uma seleção (select) para verificar a alteração na tabela
# cursor.execute('SELECT * FROM iris WHERE id = 1')
# registro_atualizado = cursor.fetchone()

# # Imprima o registro atualizado
# print("Registro Atualizado:")
# print(registro_atualizado)

# # Feche a conexão com o banco de dados
# banco.close()


# DESCOMENTE DAQUI EM DIANTE, PARA EXECUTAR 'DELETE', EM QUE SERÁ EXCLUÍDO O ID '2'

# import sqlite3

# # Função para excluir um registro na tabela 'iris' com base no ID
# def excluir_registro(cursor, id_registro):
#     cursor.execute('DELETE FROM iris WHERE id = ?', (id_registro,))

# # Conectar ao banco de dados SQLite ou criar um novo se não existir
# banco = sqlite3.connect('iris.db')
# cursor = banco.cursor()

# # Excluir um registro
# excluir_registro(cursor, 2)

# # Commit para salvar as alterações no banco de dados
# banco.commit()

# # Fechar a conexão com o banco de dados
# banco.close()


