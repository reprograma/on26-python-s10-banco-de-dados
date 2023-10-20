# Importar a biblioteca SQLite e CSV
import sqlite3
import csv

# Conectar ou criar um banco de dados chamado 'funcionarios.db'
conn = sqlite3.connect('funcionarios.db')

# Criar um objeto de cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela chamada 'funcionarios' se ela ainda não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    URL VARCHAR(255) NOT NULL,
    Name VARCHAR(100),
    Appearances INTEGER,
    Current TEXT,
    "Full Intro" TEXT,
    Year INTEGER,
    Notes TEXT
)''')

# Abrir o arquivo 'operadores.csv' para leitura
file = open("operadores.csv")

# Ignorar a primeira linha (cabeçalho) do arquivo CSV
next(file)

# Ler o conteúdo do arquivo CSV
conteudo = csv.reader(file)

# Definir a consulta SQL para inserir dados na tabela 'funcionarios'
inserir_conteudo = "INSERT INTO funcionarios (URL, Name, Appearances, Current, Gender, 'Full Intro', Year, 'Years since joining', Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Inserir os dados do arquivo CSV na tabela 'funcionarios'
cursor.executemany(inserir_conteudo, conteudo)

# Selecionar todos os registros da tabela 'funcionarios'
selecionar_tudo = "SELECT * FROM funcionarios"
entradas = cursor.execute(selecionar_tudo).fetchall()

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()