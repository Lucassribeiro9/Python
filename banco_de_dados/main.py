import sqlite3
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
DB_NAME = "sqlite.db"
DB_FILE = ROOT_FOLDER / DB_NAME
TABLE_NAME = "customers"

# Criando conexão com o banco de dados

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Criando tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)"
)

# Inserindo dados na tabela
sql_insert = f"INSERT INTO {TABLE_NAME} (name, age) VALUES (?, ?)"
cursor.execute(sql_insert, ("Alice", 30))
connection.commit()
# Fechando conexão com o banco de dados
cursor.close()
connection.close()
