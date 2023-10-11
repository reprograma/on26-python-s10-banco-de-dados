import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor ()

#cursor.execute ("CREATE TABLE pessoas (nome text, idade interger, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Aline', 35, 'email@gmail.com')") 

banco.commit ()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())