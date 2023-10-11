import sqlite3, csv

bank = sqlite3.connect('Titanic.db')
cursor = bank.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS PassengerId(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                PassengerId INTEGER NOT NULL,
                Name TEXT NOT NULL,
                Age FLOAT,
                Ticket TEXT,
                Fare FLOAT,
                Cabin TEXT,
                Embarked)''')

file = open('titanic.csv')

content = csv.reader(file)

insert_content ="INSERT INTO PassengerId (PassengerId, Name, Age, Ticket, Fare, Cabin, Embarked) VALUES (?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM PassengerId"
enter = cursor.execute(select_all).fetchall()

bank.commit()
bank.close()