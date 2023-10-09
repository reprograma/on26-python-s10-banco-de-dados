import sqlite3
import csv
banco = sqlite3.connect('Airport-Pets.db')
cursor = banco.cursor ()

cursor.execute("CREATE TABLE IF NOT EXISTS aeroportos(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Zip INTEGER NOT NULL,\
               Cidade TEXT NOT NULL,\
               Estado TEXT NOT NULL,\
               Divisão TEXT NOT NULL,\
               Estacionamento TEXT NOT NULL,\
               Pets TEXT NOT NULL,\
               Comida TEXT NOT NULL,\
               Lounge TEXT NOT NULL)")

file = open("Airport-Pets.csv")

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO aeroportos (Zip, Cidade, Estado, Divisão, Estacionamento, Pets, Comida, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM aeroportos"
entradas = cursor.execute(selecionar_tudo).fetchall();

banco.commit();
banco.close();