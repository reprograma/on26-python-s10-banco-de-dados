import sqlite3
import csv

connection = sqlite3.connect("banco_de_dados_airports_pets.db") # Criando banco de dados

cursor = connection.cursor() # Criei um cursor para executar os comandos SQL

criar_tabela = '''CREATE TABLE aeroportos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
Zip INTEGER,
City TEXT,
State TEXT,
Division TEXT,
Parking TEXT,
Pets TEXT,
Food TEXT,
Lounge TEXT
);
'''

# cursor.execute(criar_tabela)

file = open("/Users/laismeirelesalves/Estudos/semana_10/on26-python-s10-banco-de-dados/material/Airport-Pets.csv")
conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO aeroportos (Zip,City,State,Division,Parking,Pets,Food,Lounge) VALUES(?,?,?,?,?,?,?,?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * from aeroportos"

entradas = cursor.execute(selecionar_tudo).fetchall()

connection.commit()
connection.close()

# def excluir_registro(id_registro):
#     banco = sqlite3.connect('banco_de_dados_airports_pets.db')
#     cursor = banco.cursor()

#     excluir_conteudo = "DELETE FROM aeroportos WHERE = id = ?"

#     cursor.execute(excluir_conteudo(id_registro))

#     banco.commit()
#     banco.close()

# excluir_registro(4)
