#importe das bibliotecas utilizafas
import sqlite3
import csv

#criandp minha database
banco = sqlite3.connect('Airport_Pets.db')

#criacao da tabela aeroportos
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS aeroportos(\
               id INTEGER PRIMARY KEY AUTOINCREMENT, \
               Zip INTEGER NOT NULL,\
               City TEXT NOT NULL,\
               State TEXT,\
               Division TEXT,\
               Parking TEXT,\
               Pets TEXT,\
               Food TEXT,\
               Lounge TEXT)")

#abrindo arquivo csv
file = open('Airport-Pets.csv')

#pula a primeira linha do arquivo CSV, que geralmente é o cabeçalho.
next(file)

#lendo arquivo csv
conteudo = csv.reader(file)

#define a consulta SQL para inserir dados na tabela aeroportos
add_dado = "INSERT INTO aeroportos (Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"

#inserindo dadoos na database
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(37829, "França", "FC", "Southwest", "N", "Y", "Y", "N")')
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(00956, "Brasil", "BS", "Central", "Y", "Y", "N", "N")')
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(12562, "Bolivia", "BL", "Mid-Atlantic", "N", "N", "Y", "Y")')
banco.execute('INSERT INTO aeroportos(Zip, City, State, Division, Parking, Pets, Food, Lounge) VALUES(99173, "Costa Rica", "CR", "Pacific", "Y" , "Y", "Y", "N")')

#executa a consulta SQL para inserir os dados do arquivo CSV na tabela 
cursor.executemany(add_dado, conteudo)

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM aeroportos"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

banco.commit();
banco.close();

#função para editar/atualizar informações
def atualizar_dados(id_dado, novo_valor, campo):
    banco = sqlite3.connect('Airport_Pets.db')
    cursor = banco.cursor ()

#editando/atualizando informações
    banco.execute('UPDATE aeroportos SET City = "Paris" WHERE City = "França"')
    banco.execute('UPDATE aeroportos SET State = "PAR" WHERE State = "FC"')
    banco.execute('UPDATE aeroportos SET City = "São Paulo" WHERE City = "Brasil"')
    banco.execute('UPDATE aeroportos SET State = "SP" WHERE State = "BS"')

#apagando dados
def apagar_dados(id_dado):
    banco = sqlite3.connect('Airport_Pets.db')
    cursor = banco.cursor ()

#define a consulta SQL para excluir um registro com base no ID do registro
    cursor.execute('DELETE from aeroportos WHERE division = ?')

#executa a consulta SQL para excluir o registro com o ID especificado.
#o segundo argumento da função execute é uma tupla contendo o valor do ID a ser excluído.
    cursor.execute(apagar_dados, (id_dado,))

#salvar alterações no banco de dados
    banco.commit();
    banco.close();