import sqlite3
#cria o banco
banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas(nome text, idade interger, email text)")


cursor.execute("INSERT INTO pessoas VALUES ('Jani', 19, 'jani@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Jheni', 18, 'email@gmail.com')")               
cursor.execute("INSERT INTO pessoas VALUES ('Jeh', 20, 'email@gmail.com')")   
cursor.execute("INSERT INTO pessoas VALUES ('Jaime', 21, 'email@gmail.com')")   
banco.commit()


cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())
