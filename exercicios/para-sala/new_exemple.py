import sqlite3
import csv
data = sqlite3.connect('titanic.db')
cursor = data.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS passengers (\
    id integer primary key autoincrement,\
    PassengerId integer not null,\
    Name text not null,\
    Age float,\
    Ticket text,\
    Fare float,\
    Cabin text,\
    Embarked text\
)""")

file = open("titanic.csv")

content = csv.reader(file)

insert_content = "INSERT INTO passengers (PassengerId, Name, Age, Ticket, Fare, Cabin, Embarked) VALUES (?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM passengers"
inputs = cursor.execute(select_all).fetchall()

data.commit()
data.close()