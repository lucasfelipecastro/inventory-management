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
    'hiperpack': ['H742', 'H10', 'H20'],
    'goldpack': ['3L', '5L', '7L', '12L', 'PESC15', '17L', '28L']
}

for brand, codes in products.items(): 
    for code in codes:
        cursor.execute('''
            INSERT INTO Products (marca, codigo) VALUES (?, ?)
        ''', (brand, code))
        
connect.commit()
connect.close()
