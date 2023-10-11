import sqlite3
import csv

bank = sqlite3.connect("banco_de_dados_airportpets.db")
cursor = bank.cursor()

cursor.execute = ('''CREATE TABLE IF NOT EXIST airportpets (
    Id INTEGER PRIMARY KEY AUTOINCREMENT 
    Zip INT,
    City VARCHAR(100),
    State VARCHAR (2),
    Division VARCHAR(100),
    Parking YES,
    Pets YES,
    Food YES,
    Lounge YES
)''')
    

file = open("Airport-Pets.csv") #abre o arquivo .csv
next(file) #pula a 1a linha do cabeçalho pra inicar a tabela

content= csv.reader(file) #lê o arquivo contendo o csv

insert_content = "INSERT INTO airportpets (Zip,City,State,Division,Parking,Pets,Food,Lounge)\
VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, file)

select_all = "SELECT FROM * airportpets"

entry = cursor.execute(select_all).fetchall()

bank.commit()
bank.close()

#adicionar um novo pet com todas as informações necessárias
add_info = "INSERT INTO airportpets (Zip,City,State,Division,Parking,Pets,Food,Lounge)\
VALUES (01254, Rio de Janeiro, RJ, Northeast, N, Y, N, N)"

#editar um registro
uptade_info = "UPDATE airportpets" "SET Zip = 22222, State = SP" "WHERE id = 1"