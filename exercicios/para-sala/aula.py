import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Dani Negrão', 38, 'danisnegrao@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Gabii Negrão', 17, 'gabiisnegrao@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Lady Negrão', 39, 'leidisnegrao@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Paula Negrão', 29, 'paulasnegrao@gmail.com')")

banco.commit()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())