#importe das bibliotecas utilizafas
import sqlite3
import csv

#criandp minha database
banco = sqlite3.connect('Airport_Pets.db')

#criacao da tabela aeroportos
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS aeroportos(\
               id INTEGER PRIMARY KEY AUTOINCREMENT, \
               Zip INTEGER NOT NULL,\
               City TEXT NOT NULL,\
               State TEXT,\
               Division TEXT,\
               Parking TEXT,\
               Pets TEXT,\
               Food TEXT,\
               Lounge TEXT)")

#abrindo arquivo csv
file = open("Airport-Pets.csv")

#lendo arquivo csv
conteudo = csv.reader(file)

#inserindo dadpos na database
add_dado = "INSERT INTO aeroportos (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(37829, "França", "FC", "Southwest", "N", "Y", "Y", "N")')
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(00956, "Brasil", "BS", "Central", "Y", "Y", "N", "N")')
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(12562, "Bolivia", "BL", "Mid-Atlantic", "N", "N", "Y", "Y")')
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(99173, "Costa Rica", "CR", "Pacific", "Y" , "Y", "Y", "N")')

#editando informações
banco.execute('''UPDATE aeroportos SET (City = "Paris", State = "PAR" WHERE City = "França", State = "FC")''')
#UPDATE clientes SET bloqueado


#apagando dados
#DELETE FROM clientes WHERE id=4;


selecionar_tudo = "SELECT * FROM aeroportos"
entradas = cursor.execute(selecionar_tudo).fetchall

banco.commit();
banco.close();