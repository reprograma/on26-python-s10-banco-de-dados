import sqlite3

"""Cria o bando de dados"""
data = sqlite3.connect("firstData.db")

"""Esse cursor é quem executa dentro do banco de dados"""
cursor = data.cursor()

cursor.execute("CREATE TABLE peoples (name text, age integer, email text)")

cursor.execute("INSERT INTO peoples VALUES ('Cintia', 34, 'cintia.aguiar@gmail.com')")

data.commit()

cursor.execute("SELECT * FROM peoples")

print(cursor.fetchall())