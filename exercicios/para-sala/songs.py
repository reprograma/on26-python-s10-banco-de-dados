import sqlite3  # Importa o módulo sqlite3 para trabalhar com o SQLite.
import csv      # Importa o módulo csv para trabalhar com arquivos CSV.

banco = sqlite3.connect('songs.db')  # Conecta-se ou cria o banco de dados SQLite chamado 'songs.db'.
cursor = banco.cursor()              # Cria um objeto de cursor para executar comandos SQL.

# Cria a tabela 'musicas' se ela não existir, definindo a estrutura da tabela.
cursor.execute('''CREATE TABLE IF NOT EXISTS musicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    school TEXT,
    song_name TEXT,
    writers TEXT,
    year INT,
    official_song TEXT,
    sec_duration INT,
    fight TEXT,
    victory TEXT,
    colors TEXT,
    opponents TEXT,
    spelling TEXT,
    trope_count INT,
    spotify_id TEXT
)''')

file = open("songs.csv")  # Abre o arquivo CSV chamado 'songs.csv'.

# Pula a primeira linha do arquivo CSV, que geralmente é o cabeçalho.
next(file)

conteudo = csv.reader(file)  # Lê o conteúdo do arquivo CSV usando o módulo csv.

# Define a consulta SQL para inserir dados na tabela 'musicas'.
inserir_conteudo = "INSERT INTO musicas\
(school, song_name, writers, year, official_song, sec_duration, fight,\
victory, colors, opponents, spelling, trope_count, spotify_id\
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?)"

# Executa a consulta SQL para inserir os dados do arquivo CSV na tabela 'musicas'.
cursor.executemany(inserir_conteudo, conteudo)

# Define a consulta SQL para selecionar todos os registros da tabela 'musicas'.
selecionar_tudo = "SELECT * FROM musicas"

# Executa a consulta SQL para obter todas as entradas da tabela 'musicas'.
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()

"""
#função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
     banco = sqlite3.connect('songs2.db') 
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
atualizar_dado(1, 'Edilene', 'writers')
"""

"""
# #função para excluir um item
# def excluir_registro(id_registro):
#     banco = sqlite3.connect('songs3.db')
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