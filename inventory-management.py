import sqlite3

connect = sqlite3.connect('inventory.db')
cursor = connect.cursor()