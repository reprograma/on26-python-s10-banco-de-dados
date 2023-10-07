# Exercício de Sala 🏫  

## Manipulando banco de dados:

- Explicação do exercício: Esse é apenas um treinamento...
- Acessar o site do Sqlite : https://sqliteonline.com/
Digitar esses comandos diretamente no site


'''
Exemplo no site sqlite3

CREATE TABLE Test(
Id int NOT NULL,
Nome varchar(80)
);

INSERT INTO Test VALUES(1, 'Joao');

INSERT INTO Test VALUES(2, 'Maria');

INSERT INTO Test VALUES(3, 'Manuel');

SELECT * from Test

'''

Depois vamos importar o sqlite para o vscode:

'''
import sqlite3

banco = sqlite3.connect("primeiroBanco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

""" cursor.execute("INSERT INTO pessoas VALUES  ('Alguem' , 20, 'teste@email.com')")

banco.commit() """

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())

'''

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
