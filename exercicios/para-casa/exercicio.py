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

file = open("pets.csv")

next(file)

conteudo = csv.reader(file)

inserir_conteudo =  "INSERT INTO meuspets(Cod,Nome,Tipo,Genero,Idade,Peso)\
VALUES (8, Corona, Cachorro, Femea, 3, 30)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM meuspets"


entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()
