import sqlite3

banco = sqlite3.connect("primeiroBanco.db")   #db=> database aqui cria um arquivo


cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES  ('tiago fubazão' , 20, 'teste@email.com')")

banco.commit() 

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())
