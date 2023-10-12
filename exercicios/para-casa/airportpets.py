import sqlite3, csv

conecta = sqlite3.connect('''airportpets.db''')

cursor = conecta.cursor()
#Zip,City,State,Division,Parking,Pets,Food,Lounge
#21001,Aberdeen,MD,Mid-Atlantic,N,N,N,N
cursor.execute('''
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Zip INT,
    City VARCHAR(50),
    State VARCHAR(10),
    Division VARCHAR(50),
    Parking VARCHAR(10),
    Pets VARCHAR(10),
    Food VARCHAR(10),
    Lounge VARCHAR(10)
)
''')


file = open('Airport-Pets.csv')

conteudo = csv.reader(file)

inserir_conteudo = '''INSERT INTO pets (Zip,City,State,Division,Parking,Pets,Food,Lounge)\
VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = '''SELECT * FROM pets'''

entradas = cursor.execute(selecionar_tudo).fetchall()

conecta.commit()
conecta.close()