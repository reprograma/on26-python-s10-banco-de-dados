import sqlite3
import csv
banco = sqlite3.connect('PetsAeroporto.db')
cursor = banco.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS pets_airport3 (
# id INTEGER PRIMARY KEY AUTOINCREMENT,

# Zip INTEGER NOT NULL,
# City TEXT NOT NULL,
# State TEXT NOT NULL,
# Division TEXT NOT NULL,
# Parking TEXT NOT NULL,
# Pets TEXT NOT NULL,
# Food TEXT NOT NULL,
# Lounge TEXT NOT NULL               )''')

# file = open('Airport-Pets.csv')
# conteudo = csv.reader(file)

"""Adicionei algumas linhas à tabela substituindo os "?" pelos valores (estão no final da tabela)"""
# inserir_conteudo = "INSERT INTO pets_airport3 (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

# cursor.executemany(inserir_conteudo, conteudo)

# selecionar_tudo = "SELECT * FROM  pets_airport3"
# entradas = cursor.execute(selecionar_tudo).fetchall()

# banco.commit();
# banco.close();

"""Excluiu a linha de ID 851 da tabela pets_airport2"""
# def excluir_linha_em_pets_airport2(id):
#     banco = sqlite3.connect('PetsAeroporto.db')
#     cursor = banco.cursor()
#     excluir_conteudo = "DELETE FROM pets_airport2 WHERE id = ?"
#     cursor.execute(excluir_conteudo, (id, ))
#     banco.commit()
#     banco.close()

# excluir_linha_em_pets_airport2(851)

"""Atualizou o Zip Code da linha de ID 4 para 5364, na tabela pets_airport3"""
def atualizar_pets_airport3(id, novo_valor, campo):
    banco = sqlite3.connect('PetsAeroporto.db')
    cursor = banco.cursor()
    atualizar_conteudo = f"UPDATE pets_airport3 SET {campo} = ? WHERE id = ?"
    cursor.execute(atualizar_conteudo, (novo_valor, id))
    banco.commit()
    banco.close()
    

atualizar_pets_airport3(4, 5364, 'Zip')





