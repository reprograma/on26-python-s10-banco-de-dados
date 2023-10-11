import sqlite3
import csv

banco_de_dados = sqlite3.connect('aeroportopet.db')
cursor = banco_de_dados.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS listapets (
    Zip INT,
    City VARCHAR (20),
    State VARCHAR (2),
    Division VARCHAR (20),
    Parking,
    Pets,           
    Food,
    Lounge         
)''')

file = open('Airport-Pets.csv')
next(file)
leitura_arq = csv.reader(file)
inserir_novo = "INSERT INTO listapets(Zip,City,State,Division,Parking,Pets,Food,Lounge)\
VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(inserir_novo, leitura_arq)
selecionar_tudo = "SELECT * FROM listapets"
entradas = cursor.execute(selecionar_tudo).fetchall()
banco_de_dados.commit()
banco_de_dados.close()

banco_de_dados = sqlite3.connect('aeroportopet.db')
cursor = banco_de_dados.cursor()

cursor.execute("INSERT INTO listapets VALUES ('69846', 'Paulista', 'PE', 'Nordeste', 'Y','N', 'N', 'N')")
cursor.execute("INSERT INTO listapets VALUES ('16585', 'Olinda', 'PE', 'Nordeste', 'Y','Y', 'N', 'N')")
banco_de_dados.commit ()

cursor.execute("SELECT * FROM listapets")
