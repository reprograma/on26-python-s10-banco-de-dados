# Oi Professora, queria informar que fiz todas as funções em cima
# do banco de dados airportPets.db
# Fiz função por função e fui executando e deixando as outras comentadas
# recomendo que ao corrigir você vá descomentando cada função que queira usar no momento.

# Consegui fazer todas as funções solicitadas! Espero que goste, eu adorei :)


import sqlite3
import csv
banco = sqlite3.connect('airportPets.db')
cursor = banco.cursor ()
#cursor_adicionar = banco.cursor()

# Criação da Tabela

#cursor.execute('''CREATE TABLE IF NOT EXISTS airportPets (
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#Zip INTEGER NOT NULL,
#City TEXT NOT NULL,
#State TEXT,
#Division TEXT,
#Parking TEXT,
#Pets TEXT, 
#Food TEXT,
#Lounge TEXT)''')

# Leitura da Tabela

file = open("Airport-Pets.csv")

conteudo = csv.reader(file)

#Inserir o conteúdo formado por mim e também todo o conteúdo do arquivo.csv

#inserir_conteudo = "INSERT INTO airportPets (Zip, City, State, Division, Parking, Pets, Food, Lounge)  VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

#cursor.executemany(inserir_conteudo, conteudo)

#Inserir Linha Nova na Tabela

#cursor_adicionar.execute ("INSERT INTO  airportPets VALUES (2222, 'RECIFE', 'PE', 'NORDESTE', 'AMERICA-DO-SUL', 'N', 'Y', 'Y', 'Y')")

# função para atualizar um campo numa linha da tabela
#def atualizar_dado(id_registro, novo_valor, campo):
#    banco = sqlite3.connect('airportPets.db') 
#    cursor = banco.cursor()
  
#    atualizar_conteudo =  f"UPDATE airportPets SET {campo} = ? WHERE id = ?"
    

#    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
#    banco.commit()
#    banco.close()
#atualizar_dado(4, 'RECIFE', 'City')

#selecionar_tudo = "SELECT * FROM airportPets"
#entradas = cursor.execute(selecionar_tudo).fetchall()



#banco.commit()
#banco.close()

#Função DELETE (excluir um registro da tabela)

#def excluir_registro(id_registro):
#    banco = sqlite3.connect('airportPets.db')
#    cursor = banco.cursor ()
    
#    excluir_conteudo = "DELETE FROM airportPets WHERE id = ?"
  
#    cursor.execute(excluir_conteudo, (id_registro,))
    

#    banco.commit()
#    banco.close()
    

#excluir_registro(5)
#selecionar_tudo = "SELECT * FROM airportPets"
#entradas = cursor.execute(selecionar_tudo).fetchall()
#banco.close()