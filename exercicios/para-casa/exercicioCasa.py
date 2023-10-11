import sqlite3
import csv

banco = sqlite3.connect('InfoSeries3.db')
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Ranking INT NOT NULL,
    Titulo VARCHAR,
    Year INT,
    Duration FLOAT,
    Genre VARCHAR,
    Rating INT,
    Directors VARCHAR(50), 
    Votes INT NOT NULL
)''')
file = open("imdb_series.csv", encoding='utf-8-sig')
next(file)

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO series(Ranking, Titulo, Year,Duration, Genre, \
Rating , Directors, Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM series"

entradas = cursor.execute(selecionar_tudo).fetchall()
banco.commit()
banco.close()


#função para excluir um item
def excluir_registro(id_registro):
    banco = sqlite3.connect('InfoSeries3.db')
    cursor = banco.cursor ()
    excluir_conteudo = "DELETE FROM series WHERE id = ?"
    cursor.execute(excluir_conteudo, (id_registro,))
    banco.commit()
    banco.close()
    
excluir_registro(1)

#função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
      banco = sqlite3.connect('InfoSeries3.db') 
      cursor = banco.cursor() 
      atualizar_conteudo = f"UPDATE series SET {campo} = ? WHERE id = ?"
      cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
      banco.commit()
      banco.close()

atualizar_dado(2, 'Carol Ribeiro', 'Titulo')
banco.close()










