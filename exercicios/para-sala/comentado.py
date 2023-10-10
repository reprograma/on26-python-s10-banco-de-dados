# Importa as bibliotecas necessárias
import csv
import sqlite3

# Conecta-se ao banco de dados SQLite ou cria um novo se não existir
connection = sqlite3.connect("banco_de_dados_titanic.db")

# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

# Define o SQL para criar a tabela "passageiros"
criar_tabela = '''CREATE TABLE passageiros (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  PassengerId INTEGER NOT NULL,
  Name TEXT NOT NULL,
  Age FLOAT,
  Ticket TEXT,
  Fare FLOAT,
  Cabin TEXT,
  Embarked TEXT
);
'''

# Executa o comando SQL para criar a tabela
cursor.execute(criar_tabela)

# Executa o comando SQL para criar a tabela
cursor.execute(criar_tabela)

# Lê o conteúdo do arquivo CSV
conteudo = csv.reader(file)

# Define o SQL para inserir dados na tabela "passageiros"
#  Especifica as colunas da tabela nas quais desejamos inserir dados.
#  Nesse caso, estamos especificando as colunas "PassengerId", "Name", "Age", "Ticket", "Fare", "Cabin" e "Embarked".
# para indicar que os valores reais serão fornecidos posteriormente. O número de "?" corresponde ao número de colunas 
# especificadas anteriormente. Isso é feito para evitar problemas de segurança, como injeção de SQL, e também permite a
# inserção de múltiplas linhas de uma vez usando executemany.
inserir_conteudo = "INSERT INTO passageiros (PassengerId, Name, Age, Ticket, Fare, Cabin, Embarked) VALUES(?, ?, ?, ?, ?, ?, ?)"

# Executa o comando SQL para inserir os dados do CSV na tabela
cursor.executemany(inserir_conteudo, conteudo)

# Define o SQL para selecionar todos os registros da tabela "passageiros"
selecionar_tudo = "SELECT * FROM passageiros"

# Executa o comando SQL para selecionar todos os registros
entradas = cursor.execute(selecionar_tudo).fetchall()

# Comita as alterações no banco de dados e fecha a conexão
connection.commit()
connection.close()

# Abre uma nova conexão com o banco de dados
connection = sqlite3.connect("banco_de_dados_titanic.db")
cursor = connection.cursor()

# Define o SQL para selecionar todos os registros da tabela "passageiros" novamente
cursor.execute("SELECT * FROM passageiros")

# Abre um arquivo CSV para escrita
with open("bd_titanic_output.csv", "w", newline='') as csv_file:
  csv_writer = csv.writer(csv_file)
  # Escreve a linha de cabeçalho com os nomes das colunas
  csv_writer.writerow([i[0] for i in cursor.description])
  # Escreve os dados da tabela no arquivo CSV
  csv_writer.writerows(cursor)

# Fecha a conexão com o banco de dados
connection.close()
