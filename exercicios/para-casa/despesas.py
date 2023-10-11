import sqlite3
import csv

banco = sqlite3.connect('despesas.db')  
cursor = banco.cursor()     

cursor.execute('''CREATE TABLE IF NOT EXISTS despesas (
                  id INTEGER PRIMARY KEY,
                  data TEXT,
                  valor INT,
                  descricao TEXT)''')

inserir_conteudo = "INSERT INTO despesas(Data, Valor, Descricao)\
VALUES (?, ?, ?, ?, ?, ?)"


with open("despesas.csv") as file:
    conteudo = csv.reader(file)


banco.commit()
banco.close()