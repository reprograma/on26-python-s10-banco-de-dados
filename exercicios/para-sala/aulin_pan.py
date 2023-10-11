import sqlite3

banco = sqlite3.connect("Banquinho_pan.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
cursor.execute("INSERT INTO pessoas VALUES ('Mirley' , 26, 'mirleymesquita9@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Mesquita' , 26, 'mirleymesquita9@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Coelho' , 26, 'mirleymesquita9@email.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Nunes' , 26, 'mirleymesquita9@email.com')")
banco.commit()
cursor.execute("SELECT * FROM pessoas") 
print(cursor.fetchall()) #fetchall vai printar de uma maneira tabela

