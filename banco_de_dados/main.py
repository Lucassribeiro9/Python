import sqlite3
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
DB_NAME = "sqlite.db"
DB_FILE = ROOT_FOLDER / DB_NAME
TABLE_NAME = "customers"

# Criando conexão com o banco de dados

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)"
)


# Fechando conexão com o banco de dados
cursor.close()
connection.close()
