# Importar o módulo sqlite3 para trabalhar com o SQLite em Python.
import sqlite3

# Criar uma conexão com o banco de dados "primeiroBanco.db" ou criá-lo se ele não existir.
banco = sqlite3.connect("primeiroBanco.db")

# Criar um objeto cursor para executar comandos SQL no banco de dados.
cursor = banco.cursor()

# Criar uma tabela chamada "pessoas" com três colunas: nome (texto), idade (inteiro) e email (texto).
# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# # Inserir um registro na tabela "pessoas" com os valores 'Josefa', 20 e 'josefa@email.com'.
# cursor.execute("INSERT INTO pessoas VALUES ('Josefa', 20, 'josefa@email.com')")
# cursor.execute("INSERT INTO pessoas VALUES('Kerla', 23, 'ker@email.com')")
# cursor.execute("INSERT INTO pessoas Values('Zan', 23, 'zan@email.com')")

# Confirmar as alterações no banco de dados (efetuar o commit).
banco.commit()

# Executar uma consulta (SELECT) para recuperar todos os registros da tabela "pessoas".
cursor.execute("SELECT * FROM pessoas")

# Recuperar todos os registros da consulta e armazená-los em uma lista.
#fetch do inglês buscar no sentido de trazer, fetch all: trazer tudo
registros = cursor.fetchall()

# Imprimir os registros recuperados.
print(registros)