import sqlite3
import csv

#banco de dados de documentários populares em 2022 na plataforma Netflix

banco = sqlite3.connect('documentarios_netflix.db')
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS documentaries (
                Id INTEGER PRIMARY KEY,
                Title TEXT NOT NULL,
                Premiere TEXT NOT NULL,
                Runtime TEXT NOT NULL,
                Language TEXT)
               ''')
#Eu tenho direto aquele problema dele não achar o arquivo, descobri essa solução
file = open("C:\\Users\\nargy\\Documents\\estudos-semana10\\on26-python-s10-banco-de-dados\\exercicios\\para-casa\\Documentaries.csv")
conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO documentaries (Title, Premiere, Runtime, Language) VALUES (?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM documentaries"
cursor.execute(selecionar_tudo)
entradas = cursor.fetchall()

#função de excluir alguma linha com base no ID

def excluir_registro(id):
    cursor.execute("DELETE FROM documentaries WHERE Id = ?", (id,))

excluir_registro(1)
excluir_registro(2)

#testei e percebi que funciona. vou estudar mais para que se torne mais funcional e seja possível excluir várias de uma vez.

banco.commit()
banco.close()