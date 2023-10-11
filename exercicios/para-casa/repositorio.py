import sqlite3  # Importa o módulo sqlite3 para trabalhar com o SQLite.
import csv      # Importa o módulo csv para trabalhar com arquivos CSV.

#Conecta-se ao banco de dados SQLite chamado 'repositorio.db' ou cria-o se não existir.
banco = sqlite3.connect('repositorios.db')

# Cria um objeto de cursor para executar comandos SQL.
cursor = banco.cursor()

# Cria a tabela 'repositorios' se ela não existir, definindo a estrutura da tabela.
cursor.execute('''CREATE TABLE IF NOT EXISTS repositorios(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR (100),
    Description VARCHAR (100),
    URL VARCHAR (100),
    Created_at DATETIME,
    Updated_at DATETIME,
    Homepage VARCHAR (100),
    Size INTEGER,
    Stars INTEGER,
    Forks INTEGER,
    Issues INTEGER,
    Watchers INTEGER,
    Language VARCHAR (100),
    License VARCHAR (100),
    Topics VARCHAR (100),
    Has_issues BOOLEAN,
    Has_projects BOOLEAN,
    Has_downloads BOOLEAN,
    Has_wiki BOOLEAN,
    Has_pages BOOLEAN,
    Has_discussions BOOLEAN,
    Is_fork BOOLEAN,
    Is_archived BOOLEAN,
    Is_template BOOLEAN,
    Default_branch VARCHAR (100)
)''')


# Abre o arquivo CSV chamado "repositories.csv" com a codificação 'utf-8'.
file = open("repositories.csv", encoding="utf-8")

# Pula a primeira linha do arquivo CSV, que geralmente é o cabeçalho.
next(file)

# Lê o conteúdo do arquivo CSV usando o módulo csv.
conteudo = csv.reader(file)

# Define a consulta SQL para inserir dados na tabela 'repositorios'.
#como o Id foi criado e será incremento ele não rpecisa ser inserido. 
inserir_conteudo = "INSERT INTO repositorios (Name, Description, URL, Created_at, Updated_at, Homepage, Size, Stars, Forks, Issues, Watchers, Language, License, Topics, Has_issues, Has_projects, Has_downloads, Has_wiki, Has_pages, Has_discussions, Is_fork, Is_archived, Is_template, Default_branch) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Execute a consulta SQL com os valores formatados.
cursor.executemany(inserir_conteudo, conteudo)


# Define a consulta SQL para selecionar todos os registros da tabela.
selecionar_tudo = "SELECT * FROM repositorios"

# Executa a consulta SQL para obter todas as entradas da tabela.
entradas = cursor.execute(selecionar_tudo).fetchall()

# Realiza o commit para salvar as alterações no banco de dados.
banco.commit()

# Fecha a conexão com o banco de dados.
banco.close()

#######################

# função para excluir um item
def excluir_registro(id_registro):
    banco = sqlite3.connect('repositorios.db')
    cursor = banco.cursor ()
    
    # Define a consulta SQL para excluir um registro com base no ID do registro.
    excluir_conteudo = "DELETE FROM repositorios WHERE ID = ?"
    
    # Executa a consulta SQL para excluir o registro com o ID especificado.
    # O segundo argumento da função execute é uma tupla contendo o valor do ID a ser excluído.
    cursor.execute(excluir_conteudo, (id_registro,))
    
    # Salva as alterações no banco de dados.
    banco.commit()
    banco.close()
    
#chamando a função para atualizar os dados
excluir_registro(1)
banco.close()

#função para atualizar um dado
def atualizar_dado(id_registro, novo_valor, campo):
    banco = sqlite3.connect('repositorios.db') 
    cursor = banco.cursor() 
    
    # Define a consulta SQL para atualizar o valor de um campo específico em uma linha com base no ID do registro.
    # O f-string (f"UPDATE vendinhas SET {campo} = ? WHERE id = ?") permite inserir dinamicamente o nome do campo a ser atualizado.
    atualizar_conteudo = f"UPDATE repositorios SET {campo} = ? WHERE ID = ?"
    
    # Executa a consulta SQL para atualizar o valor do campo especificado na linha com o ID especificado.
    # Os valores a serem substituídos nos marcadores de posição (?) são passados como uma tupla no segundo argumento da função execute.
    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    
    # Salva as alterações no banco de dados.
    banco.commit()
    banco.close()

#chamando a função para atualizar os dados
atualizar_dado(2,'Melhor Turma do mundo','Name')
banco.close()
