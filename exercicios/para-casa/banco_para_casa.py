# Importa as bibliotecas necessárias
import csv
import sqlite3

# Conecta-se ao banco de dados SQLite ou cria um novo se não existir
bank = sqlite3.connect("banco_de_dados_songs.db")

# Cria um cursor para executar comandos SQL
cursor = bank.cursor()

# Define o SQL para criar a tabela "músicas"
criar_tabela = '''CREATE TABLE songs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  School TEXT NOT NULL,
  Song_name TEXT NOT NULL,
  Writers TEXT NOT NULL,
  Year INTEGER,
  Official_song TEXT,
  Sec_duration INTEGER,
  Fight TEXT,
  Victory TEXT, 
  Colors TEXT,
  Opponents TEXT,
  Spelling TEXT,
  Trope_count INTEGER,
  Spotify_id TEXT
);
'''
# Executa o comando SQL para criar a tabela
cursor.execute(criar_tabela)

# Abre o arquivo CSV para leitura
file = open("songs.csv")

# Lê o conteúdo do arquivo CSV
conteudo = csv.reader(file)

# Define o SQL para inserir dados na tabela "músicas"
#  Especifica as colunas da tabela nas quais desejamos inserir dados.
#  Nesse caso, estamos especificando as colunas "School", "Song_name", "Writers", "Year", "Official_song", "Sec_duration", "Fight", "Victory", "Colors", "Opponents", "Spelling", "Trope_count" e "Spotify_id".
# para indicar que os valores reais serão fornecidos posteriormente. O número de "?" corresponde ao número de colunas 
# especificadas anteriormente. Isso é feito para evitar problemas de segurança, como injeção de SQL, e também permite a
# inserção de múltiplas linhas de uma vez usando executemany.
inserir_conteudo = "INSERT INTO musicas (School, Song_name, Writers, Year, Official_song, Sec_duration, Fight, Victory, Colors, Opponents, Spelling, Trope_count, Spotify_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Executa o comando SQL para inserir os dados do CSV na tabela
cursor.executemany(inserir_conteudo, conteudo)

# Define o SQL para selecionar todos os registros da tabela "musicas"
selecionar_tudo = "SELECT * FROM musicas"

# Executa o comando SQL para selecionar todos os registros
entradas = cursor.execute(selecionar_tudo).fetchall()

# Comita as alterações no banco de dados e fecha a conexão
bank.commit()
bank.close()


