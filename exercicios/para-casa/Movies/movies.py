import sqlite3  
import csv     

banco = sqlite3.connect('movies3.db')  # Conecta-se ou cria o banco de dados SQLite chamado 'movies.db'.
cursor = banco.cursor()              


# Cria a tabela 'movie' se ela não existir, definindo a estrutura da tabela. Mantive a primeira linha pois a tabela original não tem.
cursor.execute('''CREATE TABLE IF NOT EXISTS movie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (100),
    year INT,
    genre VARCHAR (200)   
)''')

file = open("moviewithfinaledit.csv")  

conteudo = csv.reader(file)  # Lê o conteúdo do arquivo CSV usando o módulo csv.

# Define a consulta SQL para inserir dados na tabela 'movie'.
inserir_conteudo = "INSERT INTO movie(id, name, year, genre)\
VALUES (?, ?, ?, ?)"

# Executa a consulta SQL para inserir os dados do arquivo CSV na tabela .
cursor.executemany(inserir_conteudo, conteudo)

# Define a consulta SQL para selecionar todos os registros da tabela .
selecionar_tudo = "SELECT * FROM movie"

# Executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall()

banco.commit()
banco.close()

# Excluindo a linha 1, index 0, criando um novo banco

def excluir_registro(id_registro):
    banco = sqlite3.connect('movies2.db')
    cursor = banco.cursor ()
    excluir_conteudo = "DELETE FROM movie WHERE id = ?"
    cursor.execute(excluir_conteudo, (id_registro,))
    

    banco.commit()
    banco.close()
    

excluir_registro(0)
banco.close()

# Alterando o nome da linha 3 

def atualizar_dado(id_registro, novo_valor, campo):
    banco = sqlite3.connect('movies3.db') 
    cursor = banco.cursor() 
    atualizar_conteudo = f"UPDATE movie SET {campo} = ? WHERE id = ?"
    
    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    

    banco.commit()
    banco.close()
    
# Chamando a função para atualizar os dados 
atualizar_dado(3, 'Toy Story',  'name')
atualizar_dado(3, 1997, 'year')
atualizar_dado(3, 'Animation', 'Genre' )
banco.close()
