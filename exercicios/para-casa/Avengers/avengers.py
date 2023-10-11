import sqlite3
import csv

banco = sqlite3.connect('avengers.db')
cursor = banco.cursor ()


cursor.execute('''CREATE TABLE IF NOT EXISTS dados_avengers (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     URL TEXT,
     Name TEXT ,
     Appearances INT,
     Current TEXT,
     Gender TEXT,
     "Full Intro" TEXT, 
     Year INT,
     "Years since joining" INT,
     Notes TEXT
)''')

file = open("avengers.csv")
# Pula a primeira linha do arquivo CSV, que geralmente é o cabeçalho.
next(file)

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO dados_avengers\
(URL,Name,Appearances,Current,Gender,'Full Intro',\
Year,'Years since joining',Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM dados_avengers"
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()

