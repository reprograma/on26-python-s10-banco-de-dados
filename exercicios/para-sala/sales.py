import sqlite3  # Importa o módulo sqlite3 para trabalhar com o SQLite.
import csv      # Importa o módulo csv para trabalhar com arquivos CSV.

banco = sqlite3.connect('faturamento.db')  # Conecta-se ou cria o banco de dados SQLite chamado 'songs.db'.
cursor = banco.cursor()              # Cria um objeto de cursor para executar comandos SQL.


# Cria a tabela 'musicas' se ela não existir, definindo a estrutura da tabela.
# cursor.execute('''CREATE TABLE IF NOT EXISTS vendinhas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Rank INT,
#     Name VARCHAR (100),
#     Platform VARCHAR (10),
#     year INT,
#     Genre VARCHAR (20),
#     Publisher VARCHAR (20)    
# )''')

# file = open("sales.csv")  # Abre o arquivo CSV chamado 'sales.csv'.

# # Pula a primeira linha do arquivo CSV, que geralmente é o cabeçalho.
# next(file)

# conteudo = csv.reader(file)  # Lê o conteúdo do arquivo CSV usando o módulo csv.

# # Define a consulta SQL para inserir dados na tabela 'vendinhas'.
# inserir_conteudo = "INSERT INTO vendinhas(Rank,Name,Platform,Year,Genre,Publisher)\
# VALUES (?, ?, ?, ?, ?, ?)"

# # Executa a consulta SQL para inserir os dados do arquivo CSV na tabela .
# cursor.executemany(inserir_conteudo, conteudo)

# # Define a consulta SQL para selecionar todos os registros da tabela .
# selecionar_tudo = "SELECT * FROM vendinhas"

# # Executa a consulta SQL para obter todas as entradas da tabela .
# entradas = cursor.execute(selecionar_tudo).fetchall()

# banco.commit()
# banco.close()



# #função para excluir um item
# def excluir_registro(id_registro):
#      banco = sqlite3.connect('faturamento.db')
#      cursor = banco.cursor ()
    
# #     # Define a consulta SQL para excluir um registro com base no ID do registro.
#      excluir_conteudo = "DELETE FROM vendinhas WHERE id = ?"
    
# #     # Executa a consulta SQL para excluir o registro com o ID especificado.
# #     # O segundo argumento da função execute é uma tupla contendo o valor do ID a ser excluído.
#      cursor.execute(excluir_conteudo, (id_registro,))
    
# #     # Salva as alterações no banco de dados.
#      banco.commit()
#      banco.close()
    
# # #chamando a função para atualizar os dados
# excluir_registro(4)
# banco.close()


# #função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
      banco = sqlite3.connect('faturamento.db') 
      cursor = banco.cursor() 
    
#     # Define a consulta SQL para atualizar o valor de um campo específico em uma linha com base no ID do registro.
#     # O f-string (f"UPDATE musicas SET {campo} = ? WHERE id = ?") permite inserir dinamicamente o nome do campo a ser atualizado.
      atualizar_conteudo = f"UPDATE vendinhas SET {campo} = ? WHERE id = ?"
    
#     # Executa a consulta SQL para atualizar o valor do campo especificado na linha com o ID especificado.
#     # Os valores a serem substituídos nos marcadores de posição (?) são passados como uma tupla no segundo argumento da função execute.
      cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    
#     # Salva as alterações no banco de dados.
      banco.commit()
      banco.close()
    
# #chamando a função para atualizar os dados
atualizar_dado(1, 'TurmaOn26', 'Name')
banco.close()




