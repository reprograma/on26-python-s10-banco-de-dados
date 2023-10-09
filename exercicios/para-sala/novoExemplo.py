import sqlite3
import csv
banco = sqlite3.connect('titanic.db')
cursor = banco.cursor ()

cursor.execute("CREATE TABLE IF NOT EXISTS passageiros(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               PassageiroId INTEGER NOT NULL,\
               Nome TEXT NOT NULL,\
               Idade FLOAT,\
               Ticket TEXT,\
               Tarifa FLOAT,\
               Cabine TEXT,\
               Embarque TEXT)")

file = open("titanic.csv")

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO passageiros (PassageiroId, Nome, Idade, Ticket, Tarifa, Cabine, Embarque) VALUES (?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM passageiros"
entradas = cursor.execute(selecionar_tudo).fetchall();

banco.commit();
banco.close();