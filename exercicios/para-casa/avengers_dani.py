import sqlite3
import csv

banco = sqlite3.connect('marvel_dani.db')
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS marvel_av(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                URL TEXT,\
                Name TEXT ,\
                Appearances INT,\
                Current TEXT,\
                Gender TEXT,\
                "Full Intro" TEXT, \
                Year INT,\
                "Years since joining" INT,\
                 Notes TEXT)''')


file = open("avengers.csv")

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO marvel_av\
(URL,Name,Appearances,Current,Gender,'Full Intro',\
Year,'Years since joining',Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM marvel_av"
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()