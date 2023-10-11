import sqlite3
import csv

banco = sqlite3.connect('titanic.db')
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS passageiros (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                PassageiroID INTEGER NOT NULL,
                Name TEXT NOT NULL,
                Age FLOAT,
                Ticket TEXT,
                Tarifa FLOAT,
                Cabine TEXT,
                Embarque TEXT)''')

file = open("C:\\Users\\nargy\\Documents\\estudos-semana10\\on26-python-s10-banco-de-dados\\material\\titanic.csv")
conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO passageiros (PassageiroID, Name, Age, Ticket, Tarifa, Cabine, Embarque) VALUES (?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM passageiros"
cursor.execute(selecionar_tudo)
entradas = cursor.fetchall()

banco.commit()
banco.close()

