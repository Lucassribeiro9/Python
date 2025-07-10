import sqlite3
from utils import DB_FILE, TABLE_NAME

# Criando conexão com o banco de dados

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Criando tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)"
)

# Inserindo dados na tabela
sql_insert = f"INSERT INTO {TABLE_NAME}" "(name, age)" "VALUES " "(:name, :age)"
cursor.execute(
    sql_insert,
    [
        {
            "name": "Joana",
            "age": 25,
        },
        {
            "name": "Rafaela",
            "age": 30,
        },
        {"name": "Ana", "age": 22},
    ],
)
connection.commit()

# Deletando dados da tabela
cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = 3")
connection.commit()

# Atualizando dados da tabela
cursor.execute(f"UPDATE {TABLE_NAME} SET name = 'Marcondes' WHERE id = 2")
# Fechando conexão com o banco de dados
cursor.close()
connection.close()