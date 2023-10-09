import sqlite3
import csv
banco = sqlite3.connect('avengers.db')
cursor = banco.cursor ()


cursor.execute('''CREATE TABLE IF NOT EXISTS dados_avengers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
URL TEXT,
Name TEXT ,
Appearances INT,
Current TEXT,
Gender TEXT,
"Full Intro" TEXT, 
Year INT,
"Years since joining" INT,
Notes TEXT
)''')

file = open("avengers.csv")
# Pula a primeira linha do arquivo CSV, que geralmente é o cabeçalho.
next(file)

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO dados_avengers\
(URL,Name,Appearances,Current,Gender,'Full Intro',\
Year,'Years since joining',Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM dados_avengers"
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()

"""
#função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
     banco = sqlite3.connect('avengers2.db') 
     cursor = banco.cursor() 
    
    # Define a consulta SQL para atualizar o valor de um campo específico em uma linha com base no ID do registro.
    # O f-string (f"UPDATE musicas SET {campo} = ? WHERE id = ?") permite inserir dinamicamente o nome do campo a ser atualizado.
     atualizar_conteudo = f"UPDATE musicas SET {campo} = ? WHERE id = ?"
    
    # Executa a consulta SQL para atualizar o valor do campo especificado na linha com o ID especificado.
    # Os valores a serem substituídos nos marcadores de posição (?) são passados como uma tupla no segundo argumento da função execute.
     cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    
    # Salva as alterações no banco de dados.
     banco.commit()
    
    # Fecha a conexão com o banco de dados.
     banco.close()

#chamando a função para atualizar os dados
atualizar_dado(1, 'TurmaOn26', 'name')
"""



"""
# #função para excluir um item
# def excluir_registro(id_registro):
#     banco = sqlite3.connect('avengers3.db')
#     cursor = banco.cursor ()
    
#     # Define a consulta SQL para excluir um registro com base no ID do registro.
#     excluir_conteudo = "DELETE FROM musicas WHERE id = ?"
    
#     # Executa a consulta SQL para excluir o registro com o ID especificado.
#     # O segundo argumento da função execute é uma tupla contendo o valor do ID a ser excluído.
#     cursor.execute(excluir_conteudo, (id_registro,))
    
#     # Salva as alterações no banco de dados.
#     banco.commit()
    
#     # Fecha a conexão com o banco de dados.
#     banco.close()
# #chamando a função para atualizar os dados
# excluir_registro(1)
"""