import sqlite3
import csv

banco = sqlite3.connect('areopets_dani.db')
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS aero_pets(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                Zip INT,\
                City TEXT ,\
                State TEXT,\
                Division TEXT,\
                Parking TEXT,\
                Pets TEXT, \
                Food TEXT,\
                Lounge TEXT)''')


file = open("Airport-Pets.csv")

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO aero_pets\
(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM aero_pets"
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()