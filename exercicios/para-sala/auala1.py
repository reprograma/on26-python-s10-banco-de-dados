import sqlite3

banco = sqlite3.connect("primeiroBanco.db")
#conectar no banco caso exista

cursor = banco.cursor()
#cursor - manipula o banco (exercutar, etc...)

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")


cursor.execute("INSERT INTO pessoas VALUES ('Taianne' , 20, 'teste@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Joaquim' , 7, '123@.com')")
banco.commit() 

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())