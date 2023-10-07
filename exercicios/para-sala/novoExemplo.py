import sqlite3
import csv

banco = sqlite3.connect('titanic.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS passageiros(\
               id INTEGER PRIMARY KEY AUTOINCREMENT, \
               PassageiroId INTEGER NOT NULL, \
               Name TEXT NOT NULL, \
               Age FLOAT, \
               Ticket TEXT, \
               Tarifa FLOAT, \
               Cabine TEXT, \
               Embarque Text)")

file = open("titanic.csv")
conteudo = csv.reader(file)
inserir_conteudo = "INSERT INTO passageiros (PassageiroId, Name, Age, Ticket, Tarifa, Cabine, Embarque) VALUES(?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM passageiros"
entradas = cursor.execute(selecionar_tudo).fetchall

banco.commit();
banco.close();