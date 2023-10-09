import sqlite3

#kaggle = é uma pagina de DataSet, iremos utilizar muito. Nessa atividade vamos utilizar o titanic. 

#aqui estamos mexendo no sqlite dentro de python

            #Esse connect é para dizermos que queremos conectar o arquivo python com o sqlite3
banco = sqlite3.connect("primeiro_banco.db")

#criar a variável cursor, que é com ela que iremos manipular nosso banco de dados.
                    #dentro desse () vamos dar as instruções do que ele deve fazer. 
                    #ex: cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email text)")
cursor = banco.cursor()
                                            #cada coluna eu digo qual vai ser o tipo dele. (text(texto), integer(inteiro))
               #crie uma tabela chamada "pessoas" onde tem as colunas: nome, idade email                             
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

#agora vamos colocar dados nessa tabela 
                    #coloca na tabela "pessoas" os valores: 

cursor.execute("INSERT INTO pessoas VALUES ('Thaysa', 20, 'thaysa@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Kerla', 34, 'kerla@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Joana', 21, 'joana@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES ('Tatiana', 23, 'tatiana@gmail.com')")

banco.commit()
        #esse commit é que nem no github, serve para ele subir para a tabela "pessoas" que criamos. 
#então ele fala: banco (que foi o nome do arquivo de banco de dados que criamos) lança para mim esse dados que eu coloquei na tabela.

               #selecione tudo (*) de pessoas (tabela) 
cursor.execute("SELECT * FROM pessoas")

            #fetchall do inglês, trazer, trazer tudo, trazer tudo bonitinho
print(cursor.fetchall()) #apenas para ver se deu certo. 
                #esse fetchall serve para ele printar de maneira tabular "bonitinha"

                #[('Thaysa', 20, 'thaysa@gmail.com'), ('Kerla', 34, 'kerla@gmail.com'), ('Joana', 21, 'joana@gmail.com'), ('Tatiana', 23, 'tatiana@gmail.com')] -> saída

#nesse momento, a partir que rodarmos pela primeira vez temos que comentar onde criamos a tabela (linha 16), e ele criou um arquivo.py chamado primeiro_banco.db que na linha 8 eu pedi para criar. 




#agora como vamos vizualizar a tabela que criamos? 

#command shift p, abre uma pesquisa la em cima

#clicamos em Open DataBase, e vai entrar o nosso arquivo "primeiro_banco.db" dentro de uma janela aqui na esquerda chamada SQLITE EXPLORE 

#vai mostrar os database q estivemos, no nosso caso vai ser o primeiro_banco.db, e lá só rodar no play e vai mostrar a tabela certinha, aqui na direita. ->>>
