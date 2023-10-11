import sqlite3
import csv

banco = sqlite3.connect('Airport-Pets.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS airport(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                Zip INTEGER NOT NULL,\
                City TEXT NOT NULL,\
                State TEXT,\
                Division TEXT,\
                Parking TEXT,\
                Pets NOT NULL,\
                Food NOT NULL,\
                Lounge NOT NULL )")

file = open("Airport-Pets.csv")

next(file)

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO airport(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM airport"
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit ()
banco.close()

# função para excluir  um item - item excluido 4
def excluir_registro(id_registro):
    banco = sqlite3.connect('Airport-Pets.db')
    cursor = banco.cursor ()
    
# Define a consulta SQL para excluir um registro com base no ID do registro.
    excluir_conteudo = "DELETE FROM airport WHERE id = ?"
    
#     # Executa a consulta SQL para excluir o registro com o ID especificado.
#     # O segundo argumento da função execute é uma tupla contendo o valor do ID a ser excluído.
    cursor.execute(excluir_conteudo, (id_registro,))
    
#     # Salva as alterações no banco de dados.
    banco.commit()
    banco.close()
    
# #chamando a função para atualizar os dados
excluir_registro(4)
banco.close()


# #função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
    banco = sqlite3.connect('Airport-Pets.db') 
    cursor = banco.cursor() 
    
#     # Define a consulta SQL para atualizar o valor de um campo específico em uma linha com base no ID do registro.
#     # O f-string (f"UPDATE musicas SET {campo} = ? WHERE id = ?") permite inserir dinamicamente o nome do campo a ser atualizado.
    atualizar_conteudo = f"UPDATE airport SET {campo} = ? WHERE id = ?"
    
#     # Executa a consulta SQL para atualizar o valor do campo especificado na linha com o ID especificado.
#     # Os valores a serem substituídos nos marcadores de posição (?) são passados como uma tupla no segundo argumento da função execute.
    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    
#     # Salva as alterações no banco de dados.
    banco.commit()
    banco.close()
    
# #chamando a função para atualizar os dados - Linha 1 alterando nome Aberdeen por Guarulhos
atualizar_dado(1, 'Guarulhos', 'City')
banco.close()




