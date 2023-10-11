import sqlite3
import csv

#banco de dados filmes populares em 2022 na plataforma Netflix

banco = sqlite3.connect('movies_netflix.db')
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                Id INTEGER PRIMARY KEY,
                Title TEXT NOT NULL,
                Genre TEXT NOT NULL,
                Premiere TEXT NOT NULL,
                Runtime TEXT,
                Language TEXT)
               ''')

file = open("C:\\Users\\nargy\\Documents\\estudos-semana10\\on26-python-s10-banco-de-dados\\exercicios\\para-casa\\Feature films.csv", mode="r", encoding="utf-8") 
#coloquei mode e enconding pq deu erro no código
conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO movies (Title, Genre, Premiere, Runtime, Language) VALUES (?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM movies"
cursor.execute(selecionar_tudo)
entradas = cursor.fetchall()

#função de excluir alguma linha com base no ID

def excluir_registro(id):
    cursor.execute("DELETE FROM movies WHERE Id = ?", (id,))


banco.commit()
banco.close()