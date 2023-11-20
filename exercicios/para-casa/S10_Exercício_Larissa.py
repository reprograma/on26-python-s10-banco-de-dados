# Importa as bibliotecas necessárias
import csv
import sqlite3

# Conecta-se ao banco de dados SQLite ou cria um novo se não existir
connection = sqlite3.connect("bd_glassdoor.db")

# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

# Define o SQL para criar a tabela "passageiros"
criar_tabela = '''CREATE TABLE glassdoor_jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Job_Title TEXT NOT NULL,
  Salary_Estimate TEXT,
  Job_Description TEXT,
  Rating FLOAT,
  Company_Name TEXT,
  Location TEXT,
  Size TEXT,
  Founded INT,
  Type_of_ownership TEXT,
  Industry TEXT,
  Sector TEXT,
  Revenue TEXT
);
'''

# Executa o comando SQL para criar a tabela
cursor.execute(criar_tabela)

# Abre o arquivo CSV para leitura
file = open("glassdoor_data_jobs.csv")

# Lê o conteúdo do arquivo CSV
conteudo = csv.reader(file)

# Define o SQL para inserir dados na tabela "jobs"
# Especifica as colunas da tabela nas quais desejamos inserir dados.
# O número de "?" corresponde ao número de colunas especificadas anteriormente. 
# Isso é feito para evitar problemas de segurança, como injeção de SQL, e também permite a
# inserção de múltiplas linhas de uma vez usando executemany.
inserir_conteudo = "INSERT INTO glassdoor_jobs (Job_Title, Salary_Estimate, Job_Description, Rating, Company_Name, Location, Size, Founded, Type_of_ownership, Industry, Sector, Revenue) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Executa o comando SQL para inserir os dados do CSV na tabela
cursor.executemany(inserir_conteudo, conteudo)

# Define o SQL para selecionar todos os registros da tabela "jobs"
selecionar_tudo = "SELECT * FROM glassdoor_jobs"

# Executa o comando SQL para selecionar todos os registros
entradas = cursor.execute(selecionar_tudo).fetchall()

# Comita as alterações no banco de dados e fecha a conexão
connection.commit()
connection.close()

# Abre uma nova conexão com o banco de dados
connection = sqlite3.connect("bd_glassdoor.db")
cursor = connection.cursor()

# Define o SQL para selecionar todos os registros da tabela "passageiros" novamente
cursor.execute("SELECT * FROM glassdoor_jobs")

# Abre um arquivo CSV para escrita
with open("bd_jobs_output.csv", "w", newline='') as csv_file:
  csv_writer = csv.writer(csv_file)
  # Escreve a linha de cabeçalho com os nomes das colunas
  csv_writer.writerow([i[0] for i in cursor.description])
  # Escreve os dados da tabela no arquivo CSV
  csv_writer.writerows(cursor)

# Fecha a conexão com o banco de dados
connection.close()
