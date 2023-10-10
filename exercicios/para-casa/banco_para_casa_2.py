import sqlite3, csv

bank = sqlite3.connect('Airport-Pets.db')
cursor = bank.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Passenger( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                Zip INTEGER NOT NULL, \
                City TEXT NOT NULL, \
                State TEXT, \
                Division TEXT, \
                Parking TEXT, \
                Pets TEXT, \
                Food TEXT, \
                Lounge TEXT)')

file = open('Airport-Pets.csv')

content = csv.reader(file)

insert_content = "INSERT INTO Passenger (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM Passenger"
enter = cursor.execute(select_all).fetchall()

bank.commit()
bank.close()