import sqlite3 

banco = sqlite3.connect("primeiroBanco.db")
cursor = banco.cursos()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
""" 

"""

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())