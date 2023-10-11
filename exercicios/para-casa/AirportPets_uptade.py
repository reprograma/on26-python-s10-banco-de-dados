import sqlite3
import csv

def update_data(record_id, new_value, field):
    data = sqlite3.connect('airportPets.db')
    cursor = data.cursor()

    update_content = f"UPDATE Pets SET {field} = ? WHERE id = ?"
    
    cursor.execute(update_content, (new_value, record_id))
    
    data.commit()
    data.close()
    
    update_data(51, '97702', 'Zip')
    data.close()