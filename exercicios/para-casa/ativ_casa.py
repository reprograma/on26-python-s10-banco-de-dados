import sqlite3
import csv
conn = sqlite3.connect('marvel3.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    URL VARCHAR(255) NOT NULL,
    Name VARCHAR (100),
    Appearances INTEGER,
    Current TEXT,
    Gender TEXT,
    "Full Intro" TEXT,
    Year INTEGER,
    "Years since joining" INTEGER,
    Notes TEXT
)''')

file = open("avengers.csv")
next(file)

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO personagens (URL,Name,Appearances,Current,Gender,'Full Intro',Year,'Years since joining',Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM personagens"
entradas = cursor.execute(selecionar_tudo).fetchall()

conn.commit()
conn.close()

#função para excluir um item
#def excluir_registro(id_registro):
#     conn = sqlite3.connect('marvel2.db')
#     cursor = conn.cursor()

#     excluir_conteudo = "DELETE FROM personagens WHERE id = ?"

#     cursor.execute(excluir_conteudo, (id_registro,))

#     conn.commit()
#     conn.close()

#excluir_registro(9)
#conn.close()


#função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
      conn = sqlite3.connect('marvel3.db') 
      cursor = conn.cursor() 

      atualizar_conteudo = f"UPDATE personagens SET {campo} = ? WHERE id = ?"

      cursor.execute(atualizar_conteudo, (novo_valor, id_registro))

      conn.commit()
      conn.close()

#chamando a função para atualizar os dados
atualizar_dado(1, 'TurmaOn26', 'Name')
conn.close()



