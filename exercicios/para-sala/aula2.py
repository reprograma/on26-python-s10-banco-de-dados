##Usando SQLite3:

##1 - criar uma tabela chamada amigas com as seguintes colunas: id, nome, cidade, numero .
# começamos importando o módulo do SQLite
import sqlite3

# conexão com o banco (caso não exista, é criado) - chamar a atenção das alunas para a criação do arquivo na raiz do projeto
connection = sqlite3.connect('banco.db')

# criação de tabela 'amigas' - usando CREATE TABLE na query SQL
connection.execute('CREATE TABLE amigas(id INTEGER PRIMARY KEY, nome TEXT, cidade TEXT,numero INTEGER);')

##2 - Inserir 4 registros na tabela com dados ficticíos ou gerados em sala de aula:

connection.execute('INSERT INTO amigas(nome, numero, cidade) VALUES ("Anna", 24, "João Pessoa")')
connection.execute('INSERT INTO amigas(cidade, numero, nome) VALUES ("Recife", 27, "Camila")')
connection.execute('INSERT INTO amigas(cidade, numero, nome) VALUES ("Quebec", 27, "Gabi")')
connection.execute('INSERT INTO amigas(numero, cidade, nome) VALUES (2424, "São Carlos", "Tamires")')


##3 - Selecionar todas as entradas do banco usando o objeto Cursor:

cursor = connection.execute('SELECT * FROM amigas;')
entradas = cursor.fetchall()

for linha in entradas:
    print(linha)
