import sqlite3


bank = sqlite3.connect("firstBank.db")

cursor = bank.cursor()

#cursor.execute("CREATE TABLE People (Name text, age interger, email text)")

cursor.execute("INSERT INTO People VALUES ('Beyoncé', 42, 'beyonce@yonce.com')")
cursor.execute("INSERT INTO People VALUES ('Jay-Z', 54, 'rov@lane.com')")
cursor.execute("INSERT INTO People VALUES ('Blue Ivy', 12, 'blue@ivy.com')")

bank.commit()

cursor.execute("SELECT * FROM People")

print(cursor.fetchall ())