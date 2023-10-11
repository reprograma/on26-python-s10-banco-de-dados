import sqlite3
import csv

datas_airport = sqlite3.connect("pet.db")
cursor=datas_airport.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS airport_pets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Zip INT,
    City VARCHAR(100),
    State VARCHAR(50),
    Division VARCHAR(100),
    Parking YES,
    Pets YES,
    Food YES,
    Lounge YES
)''')


file = open("Airport-Pets.csv")
next(file)

conteudo = csv.reader(file)
#inserir dados 
inserir_conteudo = "INSERT INTO airport_pets(Zip,City,State, Division,Parking,Pets,Food, Lounge)\
VALUES (?, ?, ?, ?, ?, ?,?,?)"
cursor.executemany(inserir_conteudo, conteudo)
selecionar_tudo = "SELECT * FROM airport_pets"

entradas = cursor.execute(selecionar_tudo).fetchall()

datas_airport.commit()
datas_airport.close()

#edição dos dados da base csv
def atualizar_dado(id_registro, novo_valor, campo):
    datas_airport = sqlite3.connect('pet.db') 
    datas_airport = datas_airport.cursor() 

    atualizar_conteudo = f"UPDATE airport_pets SET {campo} = ? WHERE id = ?"
    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    datas_airport.commit()
    datas_airport.close()

atualizar_dado(1, 'Florianópolis', 'City')
datas_airport.close()

#excluir dados da base csv

def excluir_registro(id_registro):
    datas_airport = sqlite3.connect('pets.db')
    cursor = datas_airport.cursor ()
    excluir_conteudo = "DELETE FROM airport_pets WHERE id = ?"
    cursor.execute(excluir_conteudo, (id_registro,))
    datas_airport.commit()
    datas_airport.close()

excluir_registro(15)
datas_airport.close()