import sqlite3
import csv

banco = sqlite3.connect('Animais.db')
manipulador_do_banco = banco.cursor()

manipulador_do_banco.execute('''CREATE TABLE animais2 (Animal TEXT,
Altura TEXT,
Peso TEXT,
Cor TEXT,
Expectativa_vida_em_anos TEXT,
Dieta TEXT,
Habitat TEXT,
Predadores TEXT,
Velocidade_média TEXT,
Países_em_que_é_encontrado TEXT,
Estado_preservação TEXT,
Família TEXT,
Período_gestação_em_dias TEXT,
Velocidade_máxima TEXT,
Estrutura_social TEXT,
Número_filhotes_por_ninhada TEXT)''')

file = open('Animal Dataset.csv')
next(file)
conteudo = csv.reader(file)


inserir_conteudo = "INSERT INTO animais2 (Animal, Altura, Peso, Cor, Expectativa_vida_em_anos, Dieta, Habitat, Predadores, Velocidade_média, Países_em_que_é_encontrado, Estado_preservação, Família, Período_gestação_em_dias, Velocidade_máxima, Estrutura_social, Número_filhotes_por_ninhada) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

manipulador_do_banco.executemany(inserir_conteudo, conteudo)

"""Inseri uma nova linha no fim da tabela"""
inserir_linha = "INSERT INTO animais2 (Animal, Altura, Peso, Cor, Expectativa_vida_em_anos, Dieta, Habitat, Predadores, Velocidade_média, Países_em_que_é_encontrado, Estado_preservação, Família, Período_gestação_em_dias, Velocidade_máxima, Estrutura_social, Número_filhotes_por_ninhada) VALUES ('a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')"
manipulador_do_banco.execute(inserir_linha)

selecionar_tudo = "SELECT * FROM  animais2"
entradas = manipulador_do_banco.execute(selecionar_tudo).fetchall()

banco.commit();
banco.close();

"""Excluí as linhas correspondentes aos animais Aardvark"""

def excluir(Animal):
    banco = sqlite3.connect('Animais.db')
    manipulador_do_banco = banco.cursor() 
    excluir_conteudo = "DELETE FROM animais2 WHERE Animal = ?"
    manipulador_do_banco.execute(excluir_conteudo, (Animal, ))
    banco.commit()
    banco.close()

#excluir("Aardvark")

"""Subtituí African Lion por Leão africano na linha 5 da tabela"""
def atualizar(Animal, novo_valor, campo):
    banco = sqlite3.connect('Animais.db')
    manipulador_do_banco = banco.cursor()
    atualizar_conteudo = f"UPDATE animais2 SET {campo} = ? WHERE Animal = ? "
    manipulador_do_banco.execute(atualizar_conteudo, (novo_valor, Animal))
    banco.commit()
    banco.close()
    

#atualizar("African Lion", "Leão africano", "Animal")

