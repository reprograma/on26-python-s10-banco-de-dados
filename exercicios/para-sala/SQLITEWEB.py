import sqlite3

CREATE TABLE Bodecam(
ID int NOT NULL,
Name varchar(80)
);
CREATE TABLE New (ID int, Name varchar (120));

INSERT INTO Bodecam VALUES(1, "Beyonce");
INSERT INTO Bodecam VALUES(2, "Bruna");
INSERT INTO Bodecam VALUES(3, "Thaysa");
INSERT INTO Bodecam VALUES(4, "Elisabete");
INSERT INTO Bodecam VALUES(5, "Joao");

SELECT  * FROM Bodecam

CREATE TABLE Employess(
ID INT PRIMARY KEY,
Name VARCHAR(255),
Salary DECIMAL(10, 2)
);

INSERT INTO Employess (ID, Name, Salary)
VALUES
(1, "Beyonce Knowles", 4000.00),
(2, "Jayz Carter", 3000.00),
(3, "Bruna Macedo", 500.00),
(4, "Elisabete Monteiro", 500.00);


SELECT * FROM Employess WHERE id = 2

CREATE TABLE Pets (
ID INT PRIMARY KEY,
Name varchar (120),
Race varchar (80),
Species varchar (20),
Castred int (1)
);

INSERT INTO Pets(ID, Name, Race, Species, Castred)
VALUES
(1, "Syndra", "SRD", "Feline", 0),
(2, "Lissandra", "Siamese", "Feline", 0),
(3, "Zed", "Yorkshire", "Dog", 0);

SELECT * FROM Pets