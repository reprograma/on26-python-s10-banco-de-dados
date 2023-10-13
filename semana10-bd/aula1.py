import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('May' , 29, 'testeemail2@email.com')")

banco.commit()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())

