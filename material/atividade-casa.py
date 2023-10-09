import sqlite3
import csv
banco = sqlite3.connect('PetsAeroporto.db')
cursor = banco.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS pets_airport (
# id INTEGER PRIMARY KEY AUTOINCREMENT,

# Zip INTEGER NOT NULL,
# City TEXT NOT NULL,
# State TEXT NOT NULL,
# Division TEXT NOT NULL,
# Parking TEXT NOT NULL,
# Pets TEXT NOT NULL,
# Food TEXT NOT NULL,
# Lounge TEXT NOT NULL               )''')

# file = open('Airport-Pets.csv')
# conteudo = csv.reader(file)

# inserir_conteudo = "INSERT INTO pets_airport (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

# cursor.executemany(inserir_conteudo, conteudo)

"""Função para adicionar uma linha por vez na tabela"""
def adicionar(informacoes):
    adicao_de_item = cursor.execute(informacoes)
    return adicao_de_item


aero_LA = "INSERT INTO pets_airport VALUES (857, 67011, 'Los Angeles', 'CA', 'Pacific', 'Y', 'Y', 'N', 'N')"
adicionar(aero_LA)

selecionar_tudo = "SELECT * FROM  pets_airport"
entradas = cursor.execute(selecionar_tudo).fetchall()



banco.commit();
banco.close();


