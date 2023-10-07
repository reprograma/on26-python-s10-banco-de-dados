import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Ana' , 21, 'teste1@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Beto' , 32, 'teste2@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Viviane' , 44, 'teste3@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Julia' , 20, 'teste4@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Caio' , 38, 'teste5@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Pedro' , 29, 'teste6@email.com')")


banco.commit() 

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())