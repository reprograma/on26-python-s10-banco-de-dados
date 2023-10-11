import sqlite3

banco = sqlite3.connect("PrimeiroBanco.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES  ('Jessica' , 33, 'jessicapaula04@gmail.com')")

banco.commit() 

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())