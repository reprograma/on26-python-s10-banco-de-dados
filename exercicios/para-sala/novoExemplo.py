import sqlite3
import csv
conn = sqlite3.connect('titanic.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS passageiros (id INTEGER PRIMARY KEY AUTOINCREMENT, PassageiroId INTEGER NOT NULL, Name TEXT NOT NULL, Age FLOAT, Ticket TEXT, Fare FLOAT, Cabin TEXT, Embarked TEXT)")

file = open("titanic.csv")

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO passageiros (PassageiroId, Name, Age, Ticket, Fare, Cabin, Embarked) VALUES (? ? ? ? ? ? ?)"

cursor.executemany(inserir_conteudo)

selecionar_tudo = "SELECT * FROM passageiros"
entradas = cursor.execute(selecionar_tudo).fetchall()

conn.commit();
conn.close();