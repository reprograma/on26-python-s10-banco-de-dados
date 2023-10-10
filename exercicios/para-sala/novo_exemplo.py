import sqlite3

banco = sqlite3.connect("segundoBanco.db")

cursor = banco.cursor ()

cursor.execute ("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Amanda', 21, 'amanda@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Brenda', 21, 'amanda@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Carla', 21, 'amanda@gmail.com')")

banco.commit ()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall ())