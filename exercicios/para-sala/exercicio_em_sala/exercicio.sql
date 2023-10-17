--criar uma tabela, com o Id que não seja nulo e com o nome varchar que pode ir até x caracter
-- o varchar ele se adequa ao espaço, já o char ele ocupa esse espaço da memoria e não se altera;
--CREATE TABLE Test(
 --Id int NOT NULL,
 --Nome varchar(80)
 --);
  
 --inserir dados na tabela
--INSERT INTO Test VALUES(1, 'Joao');
--INSERT INTO Test VALUES(2, 'Maria');
 --INSERT INTO Test VALUES(3, 'Manuela');
 
 -- visualização dos dados no dia a dia não usamos o *, para não travar
 --SELECT * FROM Test
 
---------------

--criar a tabela funcionarios, com a chave primaria, com o nome, e com o salario decimal(10 números antes da virgula, e só 2 números depois da virgula);
--CREATE TABLE Funcionarios (
--  ID INT PRIMARY KEY,
--  Nome VACHAR(255),
--  Salario Decimal(10, 2)
 --);
 
-- inserir os dados
--INSERT INTO Funcionarios (ID, Nome, Salario)
--VALUES
--	(1, 'João Silva', 3500.00),
--  (2, 'Maria José', 4500.50),
--  (3, 'Josefa Maria', 2800.00);
--  (5, 'Bruna Oliver', 7200.00),
--  (6, 'Maria Carmen', 5200.00),
--  (7, 'Teodoro Josue', 1500.00);
    
SELECT * FROM Funcionarios WHERE ID = 5;

***************************

--criar uma tabela 
--CREATE TABLE Pet(
--  Id INT PRIMARY KEY,
--  Nome VARCHAR(120),
--  Raca VARCHAR(80),
--  Especie VARCHAR(80),
--  Castrado INT (2)
--  );
  
  -- INSERIR DADOS
  --INSERT INTO Pet(ID, Nome, Raca, Especie, Castrado)
  --VALUES
  --(1, 'Bob', 'Pooble', 'Cão', 0),
  --(2, 'Hawking', 'Chiuaua', 'Cão', 1),
  --(3, 'Pingo', 'Caramelo', 'Cão', 1),
  --(4, 'Morcego', 'SRD', 'Gato', 0),
  --(5, 'Ada', 'Chiauau', 'Cão', 1);
  
  -- visualização dos dados
  SELECT * FROM Pet

-- def excluir_registro(id):
--cursor.execute("DELETE FROM documentaries WHERE Id = ?", (id,))