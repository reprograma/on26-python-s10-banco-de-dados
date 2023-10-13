import sqlite3
import csv

banco = sqlite3.connect('animals.db')
cursor = banco.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS meuspets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codpet INT,
    Nomepet VARCHAR (100),
    Tipopet VARCHAR (10),
    Generopet VARCHAR (20),
    Idadepet INT,
    Pesopet INT    
)''')

arquivo = open("pets.csv")
next(arquivo)



conteudo = csv.reader(arquivo)

inserir_conteudo =  "INSERT INTO meuspets(codpet,Nomepet,Tipopet,Generopet,Idadepet,Pesopet)\
VALUES (5, Corona, cachorro, Femea, 3, 30)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM meuspets"


entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()
