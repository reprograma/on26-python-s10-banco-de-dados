# pode executar tudo de uma só vez!

import sqlite3     # importando o módulo sqlite3 para utilizar o SQLite
import csv         # importanto o módulo csv para trabalhar com arquivos csv


# conectando/criando o banco de dados
database = sqlite3.connect('airportPets.db')

# criando um objeto de cursos para executar comandos SQL
cursor = database.cursor()

# criando a tabela "petsvoando" se ela não existir
# definindo a estrutura da tabela de acordo com o arquivo csv
cursor.execute('''CREATE TABLE IF NOT EXISTS petsvoando (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Zip INT NOT NULL,
               City VARCHAR (30) NOT NULL,
               State VARCHAR (2) NOT NULL,
               Division VARCHAR (20) NOT NULL,
               Parking VARCHAR (1),
               Pets VARCHAR (1),
               Food VARCHAR (1),
               Lounge VARCHAR (2)
)''')

# abrindo o arquivo csv chamado "table_airportPets"
file = open("airportPets.csv")

# comando para evitar que a tabela fique com dois cabeçalhos
next(file)

# lendo o conteúdo do arquivo csv com o módulo csv
conteudo = csv.reader(file)

# definindo a consulta SQL para inserir dados na tabela "petsvoando"
inserir_conteudo = "INSERT INTO petsvoando(Zip, City, State, Division, Parking, Pets, Food, Lounge)\
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

# executando a consulta SQL para inserir os dados do arquivo csv na tabela criada
cursor.executemany(inserir_conteudo, conteudo)

# definindo a consulta SQL para selecionar todos os dados inseridos na tabela
selecionar_tudo = "SELECT * FROM petsvoando"

# executando a consulta SQL para ler todos os dados inseridos na tabela criada
entradas = cursor.execute(selecionar_tudo).fetchall()

# enviando e salvando todas as ações solicitadas no banco de dados
database.commit()

# fechando o banco de dados
database.close()


# Ctrl + Shift + P para abrir o banco de dados


#INSERINDO NOVO DADO

database = sqlite3.connect('airportPets.db')
cursor = database.cursor()

# executando a consulta SQL para inserir novos dados
cursor.execute("INSERT INTO petsvoando(Zip, City, State, Division, Parking, Pets, Food, Lounge)\
                VALUES\
                ('41510045', 'Salvador', 'BA', 'Am S - Brasil', 'Y', 'Y', 'Y', 'Y'),\
                ('44069010', 'Feira de Santana', 'BA', 'Am S - Brasil', 'Y', 'N', 'Y', 'N')")

# definindo a consulta SQL para ler o(s) último(s) id(s) inserido(s) 
selecionar_insercao = "SELECT MAX(id) FROM petsvoando"    # MAX(id) traz o maior id, mas nem sempreo mais id será o último inserido

database.commit()
database.close()


# ATUALIZANDO UM DADO

# definindo a função
def atualizar_registro(id, novo_valor, campo):
    database = sqlite3.connect('airportPets.db')
    cursor = database.cursor()

    # definindo a consulta SQL para atualizar um registro com base no id
    atualizar_conteudo = f"UPDATE petsvoando SET {campo} = ? WHERE id = ?"

    # Executando a consulta SQL para inserir atualizar um dado
    cursor.execute(atualizar_conteudo, (novo_valor, id))

    database.commit()
    database.close()

# chamando a função para atualizar dado
atualizar_registro(2, 'Reprograma', 'City')
atualizar_registro(2, '{ }', 'State')
database.close()


# DELETANDO UM DADO

# definindo a função
def deletar_registro(id):
    database = sqlite3.connect('airportPets.db')
    cursor = database.cursor()
    
    # definindo a consulta SQL para excluir um registro com base no id
    excluir_conteudo = "DELETE FROM petsvoando WHERE id = ?"
    
    # executando a consulta SQL para inserir deletar um dado
    cursor.execute(excluir_conteudo, (id,))

    database.commit()
    database.close()

# chamando a função para deletar dado
deletar_registro(1)
database.close()