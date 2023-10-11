import sqlite3
banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Carol' , 43, 'teste@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Suri' , 13, 'teste@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Dan' , 44, 'teste@email.com')")



banco.commit() 

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())
