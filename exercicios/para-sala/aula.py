import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor() #cursor serve para executar o que faremos

# cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('zari', '25', 'zari@mail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('zana', '20', 'zana@mail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('zani', '22', 'zani@mail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('zare', '25', 'zare@mail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('zara', '22', 'zara@mail.com')")

banco.commit ()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall ()) #printar de uma maneira tabelar

#ctrl shift p open database
