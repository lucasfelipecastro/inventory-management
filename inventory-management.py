import sqlite3

connect = sqlite3.connect('inventory.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        marca TEXT NOT NULL,
        codigo TEXT NOT NULL)
''')

connect.commit()