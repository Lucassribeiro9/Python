import sqlite3
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
DB_NAME = "sqlite.db"
DB_FILE = ROOT_FOLDER / DB_NAME

# Criando conexão com o banco de dados

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.close()
connection.close()
