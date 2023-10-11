import sqlite3
import csv

def delete_record(record_id):
    data = sqlite3.connect('airportPets.db')
    cursor = data.cursor()

    delete_content = "DELETE FROM Pets WHERE id = ?"

    cursor.execute(delete_content, (record_id,))

    data.commit()
    data.close()

    delete_record(49)
    data.close()