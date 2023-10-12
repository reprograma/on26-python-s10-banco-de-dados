import sqlite3


def criar_banco():
    banco = sqlite3.connect('meu_banco.db')
    cursor = banco.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (
                     ID INTEGER PRIMARY KEY,
                     Nome TEXT,
                     Idade INTEGER,
                     Email TEXT
                     )''')

    banco.commit()
    banco.close()

def adicionar_pessoa(nome, idade, email):
    banco = sqlite3.connect('meu_banco.db')
    cursor = banco.cursor()

    cursor.execute("INSERT INTO pessoas (Nome, Idade, Email) VALUES (?, ?, ?)", (nome, idade, email))

    banco.commit()
    banco.close()

def editar_pessoa(id, nome, idade, email):
    banco = sqlite3.connect('meu_banco.db')
    cursor = banco.cursor()

    cursor.execute("UPDATE pessoas SET Nome = ?, Idade = ?, Email = ? WHERE ID = ?", (nome, idade, email, id))

    banco.commit()
    banco.close()

def ler_pessoas():
    banco = sqlite3.connect('meu_banco.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()

    banco.close()
    return pessoas

criar_banco()

adicionar_pessoa("Dayani", 33, "dayani@email.com")

editar_pessoa(1, "Dayani Rosa", 31, "day.rosa@email.com")

pessoas = ler_pessoas()
for pessoa in pessoas:
    print(pessoa)
