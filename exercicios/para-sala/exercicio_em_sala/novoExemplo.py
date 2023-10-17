# Importar as bibliotecas necessárias.
import sqlite3
import csv

# Conectar-se ao banco de dados "titanic.db" ou criá-lo se ele não existir.
banco = sqlite3.connect('titanic.db')

# Criar um cursor para executar comandos SQL no banco de dados.
cursor = banco.cursor()

# Criar uma tabela chamada "passageiros" com as colunas especificadas.
# A coluna "id" é definida como uma chave primária que se autoincrementa automaticamente.
cursor.execute('''CREATE TABLE IF NOT EXISTS passageiros (
id INTEGER PRIMARY KEY AUTOINCREMENT,
PassageiroId INTEGER NOT NULL,
Name TEXT NOT NULL,
Age FLOAT,
Ticket TEXT,
Fare FLOAT,
Cabin TEXT, 
Embarked TEXT)''')

# Abrir o arquivo "titanic.csv" para leitura.
file = open("titanic.csv")

# Ler o conteúdo do arquivo CSV.
conteudo = csv.reader(file)

# Preparar a consulta SQL para inserir dados na tabela "passageiros".
inserir_conteudo = "INSERT INTO passageiros (PassageiroId, Name, Age, Ticket, Fare, Cabin, Embarked) VALUES (?, ?, ?, ? ,? ,?, ?)"
# Executar a inserção de múltiplos registros do arquivo CSV na tabela.
cursor.executemany(inserir_conteudo, conteudo)

# Preparar a consulta SQL para selecionar todos os registros da tabela "passageiros".
selecionar_tudo = "SELECT * FROM passageiros"

# Executar a consulta SQL e armazenar os resultados em 'entradas'.
entradas = cursor.execute(selecionar_tudo).fetchall()

# Confirmar as alterações no banco de dados.
banco.commit();

# Fechar a conexão com o banco de dados.
banco.close();
