import sqlite3
import csv

#Criar a conexão com o banco de dados
banco = sqlite3.connect('musicas.db')
#Definir o cursor do banco 
cursor = banco.cursor()

#Pedir ao cursor pra criar um banco de dados com tais colunas
#cursor.execute("""CREATE TABLE IF NOT EXISTS musicas (
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#school TEXT NOT NULL,
#song_name TEXT NOT NULL,
#writers TEXT NOT NULL,
#year INTEGER,
#official_song TEXT NOT NULL,
#sec_duration INTEGER,
#fight TEXT NOT NULL,
#victory TEXT NOT NULL,
#colors TEXT NOT NULL,
#opponents TEXT NOT NULL,
#spelling TEXT NOT NULL,
#trope_count INTEGER,
#spotify_id TEXT NOT NULL)""")

#Definir um método da biblioteca CSV pra selecionar o arquivo
#file = open("songs.csv")

#Usar um método da biblioteca CSV pra acessar o conteúdo do CSV
#conteudo = csv.reader(file)

#Definir o INSERT pra executar mais abaixo
#inserir_conteudo = '''INSERT INTO musicas (school, song_name, writers, year, official_song, sec_duration, fight, victory, colors, opponents, spelling, trope_count, spotify_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

#Inserir conteúdo do csv no banco de dados SQL
#cursor.executemany(inserir_conteudo, conteudo)

#UPDATE de uma coluna da tabela
#cursor.execute('''UPDATE musicas SET official_song = 'Yes' WHERE official_song = 'No';''')
cursor.execute('''DELETE FROM musicas WHERE id = 5 ''')

#Selecionar o que o execute vai mostrar mais abaixo
selecionar_tudo = '''SELECT * FROM musicas'''

#SELECT pra visualizar toda a população da lista
entradas = cursor.execute(selecionar_tudo).fetchall()

for linha in entradas:
    print(linha)

#Fazer commit das mudanças no banco de dados
banco.commit()
#Encerrar a conexão
banco.close()

#Falta UPDATE e DELETE de certas infos do banco de dados