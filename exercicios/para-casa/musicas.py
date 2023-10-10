import sqlite3, csv

musica = sqlite3.connect('musicas.db')

cursor = musica.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS musicas (id INTEGER PRIMARY KEY AUTOINCREMENT, school VARCHAR(200), song_name VARCHAR(200), writers VARCHAR(200), year INT, official_song VARCHAR(10), sec_duration INT, fight VARCHAR(10), victory VARCHAR(10), colors VARCHAR(10), opponents VARCHAR(10), spelling VARCHAR(10), trope_count INT, spotify_id VARCHAR(100))")



file = open('songs.csv')

next(file)

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO musicas(school, song_name, writers, year, official_song, sec_duration, fight, victory, colors, opponents, spelling, trope_count, spotify_id)\
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM musicas"

entradas = cursor.execute(selecionar_tudo).fetchall()

musica.commit()
musica.close()


#agora vamos excluir um id: 

# def excluir_registro_id(id_registro):
#     musica = sqlite3.connect('musicas.db') 

#     cursor = musica.cursor()

#     excluir_conteudo = "DELETE FROM musicas WHERE id = ?"

#     cursor.execute(excluir_conteudo, (id_registro))

#     musica.commit()
#     musica.close()

#     excluir_registro_id(40) 
#     musica.close()


#agora vamos atualizar: 

def atualizar_dado(id_registro, novo_valor, campo,):
     musica = sqlite3.connect('musicas.db') 
     cursor = musica.cursor() 
    
     atualizar_conteudo = f"UPDATE musicas SET {campo} = ? WHERE id = ?"
    
     cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    
    # Salva as alterações no banco de dados.
     musica.commit()
     musica.close()
    
#chamando a função para atualizar os dados
atualizar_dado(1, 'Braga', 'school')

atualizar_dado(1, 'Thaysa Lima', 'song_name')

musica.close()



