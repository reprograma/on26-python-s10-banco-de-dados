import sqlite3

banco = sqlite3.connect("testeBanco.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoa (nome text, idade interger, email text)")

cursor.execute("INSERT INTO pessoa VALUES ('Julia', 15, 'julia@gmail.com')")
cursor.execute("INSERT INTO pessoa VALUES ('Maria', 29, 'maria@gmail.com')")
cursor.execute("INSERT INTO pessoa VALUES ('Jessica', 31, 'jessica@gmail.com')")

cursor.execute("SELECT * FROM pessoa")

print(cursor.fetchall())