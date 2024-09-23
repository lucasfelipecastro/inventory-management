import sqlite3

connect = sqlite3.connect('inventory.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        marca TEXT NOT NULL,
        codigo TEXT NOT NULL)
''')

connect.commit()

products = {
    'galvanotek': ['GA90', 'G695', 'G697'],
    'niagara': ['MUD1', 'MUD2', 'MUD3'],
    'hiperpack': ['H742', 'H10', 'H20']
}