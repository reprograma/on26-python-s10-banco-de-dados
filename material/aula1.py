import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email text")

cursor.execute("INSERT INTO pessoas VALUES('Nanda', 19, 'nanda@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('Sara', 16, 'sara@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('Levy', 17, 'levy@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('Hyslla', 18, 'hyslla@gmail.com')")


banco.commit()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())