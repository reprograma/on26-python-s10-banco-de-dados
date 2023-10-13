import sqlite3
import csv
connection = sqlite3.connect('maternal_mortality.db')
cursor = connection.cursor()

# Entity,Code,Year,Indicator:Maternal mortality ratio (per 100 000 live births)

cursor.execute('''CREATE TABLE IF NOT EXISTS maternal_mortality (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Entity TEXT,
               Code TEXT,
               Year TEXT, 
               Maternal_mortality_ratio FLOAT
               );''')

file = open("maternal-mortality-who.csv")

content = csv.reader(file)

insert_content = "INSERT INTO maternal_mortality (Entity,Code,Year,Maternal_mortality_ratio) VALUES(?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM maternal_mortality"
entry = cursor.execute(select_all).fetchall()

connection.commit()
connection.close()