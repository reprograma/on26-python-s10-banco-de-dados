import sqlite3  
import csv      

banco = sqlite3.connect('voos.db')  # Criando o banco de dados "voo.db"
cursor = banco.cursor()              

# Criei a tabela "destinos" se ela não existir 
cursor.execute(''' CREATE TABLE IF NOT EXISTS destinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Country VARCHAR (100),
    "Airline passengers carried" FLOAT,
    Year INT
       
)''')

file = open("airline.csv")  # O arquivo "airline.csv" foi baixado do Kaggle


next(file)

conteudo = csv.reader(file)  


inserir_conteudo = "INSERT INTO destinos(Country, 'Airline passengers carried', Year)\
VALUES (?, ?, ?)" # A tabela possui três campos


cursor.executemany(inserir_conteudo, conteudo)


selecionar_tudo = "SELECT * FROM destinos"


entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()