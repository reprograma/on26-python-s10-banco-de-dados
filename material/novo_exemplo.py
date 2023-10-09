import sqlite3
import csv

banco = sqlite3.connect('titanic.db')
cursor = banco.cursor()

# Cria a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS passageiros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    PassengerId INTEGER NOT NULL,
    Name TEXT NOT NULL,
    Age FLOAT,
    Ticket TEXT,
    Fare FLOAT,
    Cabin TEXT, 
    Embarked TEXT)''')

file = open("titanic.csv")
conteudo = csv.reader(file)

# Pule o cabeçalho do CSV
next(conteudo)

# Itera sobre as linhas do arquivo CSV e insere os dados na tabela
for row in conteudo:
    # Verifique se os valores não estão vazios antes de tentar converter
    PassengerId = int(row[0])
    Name = row[1]
    Age = float(row[2]) if row[2] else None
    Ticket = row[3]
    
    # Remova os pontos do campo "Fare" e converta em float
    Fare = float(row[4].replace('.', '').replace(',', '.')) if row[4] else None
    
    Cabin = row[5]
    Embarked = row[6]
    
    cursor.execute("INSERT INTO passageiros (PassengerId, Name, Age, Ticket, Fare, Cabin, Embarked) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (PassengerId, Name, Age, Ticket, Fare, Cabin, Embarked))

banco.commit()
banco.close()
