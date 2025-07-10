import sqlite3
from utils import DB_FILE, TABLE_NAME

# Criando conexão com o banco de dados

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")
for row in cursor.fetchall():
    _id, name, age = row
    print(f"ID: {_id}, Name: {name}, Age: {age}")
print()

cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = 2")
row = cursor.fetchone()
_id, name, age = row
print(f"id: {_id}, Name: {name}, Age: {age}")

cursor.close()
connection.close()
