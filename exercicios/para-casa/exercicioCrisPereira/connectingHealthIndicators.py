import sqlite3
import csv
connection = sqlite3.connect('health_indicators.db')
cursor = connection.cursor()

# VAR,"Variable","UNIT","Measure","COU","Country","YEA","Year","Value","Flag Codes","Flags"

cursor.execute('''CREATE TABLE IF NOT EXISTS pharmaceuticals (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               VAR TEXT,
               Variable TEXT,
               UNIT TEXT,
               Measure TEXT,
               COU TEXT,
               Country TEXT,
               YEA TEXT,
               Year TEXT, 
               Value FLOAT,
               Flag_Codes TEXT,
               Flags TEXT
               );''')

file = open("health_indicators_ocde.csv")

content = csv.reader(file)

insert_content = "INSERT INTO pharmaceuticals (VAR,Variable,UNIT,Measure,COU,Country,YEA,Year,Value,Flag_Codes,Flags) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM pharmaceuticals"
entry = cursor.execute(select_all).fetchall()

connection.commit()
connection.close()