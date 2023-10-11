##Prof. os exercícios extras estão em funções separadas, que seguem:
#Delete = AirportPets_delete.py
#Update = AirportPets_update.py

import sqlite3
import csv

#Create 
data = sqlite3.connect('airportPets.db')
cursor = data.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Pets (\
    id integer primary key autoincrement,\
    Zip integer not null,\
    City text not null,\
    State text,\
    Division text,\
    Parking text,\
    Pets text,\
    Food text,\
    Lounge text\
)""")

#Insert
file = open("Airport-Pets.csv")
next(file)

content = csv.reader(file)
insert_content = "INSERT INTO Pets (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(insert_content, content)

#Select 
select_all = "SELECT * FROM Pets"
inputs = cursor.execute(select_all).fetchall()

data.commit()
data.close()