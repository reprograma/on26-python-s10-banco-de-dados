import sqlite3
import csv

banco = sqlite3.connect('Animais.db')
manipulador_do_banco = banco.cursor()

# manipulador_do_banco.execute('''CREATE TABLE animais_atualizar (Animal TEXT,
# Altura TEXT,
# Peso TEXT,
# Cor TEXT,
# Expectativa_vida_em_anos TEXT,
# Dieta TEXT,
# Habitat TEXT,
# Predadores TEXT,
# Velocidade_média TEXT,
# Países_em_que_é_encontrado TEXT,
# Estado_preservação TEXT,
# Família TEXT,
# Período_gestação_em_dias TEXT,
# Velocidade_máxima TEXT,
# Estrutura_social TEXT,
# Número_filhotes_por_ninhada TEXT)''')

file = open('Animal Dataset.csv')
next(file)
conteudo = csv.reader(file)

"""Inseri uma última linha na tabela com o animal Boi"""
inserir_conteudo = "INSERT INTO animais2 (Animal, Altura, Peso, Cor, Expectativa_vida_em_anos, Dieta, Habitat, Predadores, Velocidade_média, Países_em_que_é_encontrado, Estado_preservação, Família, Período_gestação_em_dias, Velocidade_máxima, Estrutura_social, Número_filhotes_por_ninhada) VALUES ('Boi', 'baixo', 'pesado', 'marrom', 'muitos', 'grama', 'pastos', 'talvez uma jiboia', 'devagar e sempre', 'praticamente todos', 'conservado', 'disfuncional', '0', 'devagar', 'sempre com amigos', '0')"

manipulador_do_banco.execute(inserir_conteudo)

selecionar_tudo = "SELECT * FROM  animais2"
entradas = manipulador_do_banco.execute(selecionar_tudo).fetchall()

banco.commit();
banco.close();

"""Excluí as linhas correspondentes aos animais Aardvark e Anteater"""

def excluir(Animal):
    banco = sqlite3.connect('Animais.db')
    manipulador_do_banco = banco.cursor() 
    excluir_conteudo = "DELETE FROM animais_excluir_linha WHERE Animal = ?"
    manipulador_do_banco.execute(excluir_conteudo, (Animal, ))
    banco.commit()
    banco.close()

#excluir("Aardvark")

"""Subtituí African Lion por Leão africano na linha 5 da tabela"""
def atualizar(Animal, novo_valor, campo):
    banco = sqlite3.connect('Animais.db')
    manipulador_do_banco = banco.cursor()
    atualizar_conteudo = f"UPDATE animais_atualizar SET {campo} = ? WHERE Animal = ? "
    manipulador_do_banco.execute(atualizar_conteudo, (novo_valor, Animal))
    banco.commit()
    banco.close()
    

#atualizar("African Lion", "Leão africano", "Animal")

