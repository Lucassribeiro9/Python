import os

import pymysql
from dotenv import load_dotenv

load_dotenv()
# Load environment variables from .env file
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
)
TABLE_NAME = "customers"

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL)"
        )
    connection.commit()
    # insert
    with connection.cursor() as cursor:
        result = cursor.execute(
            f"INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)",
            ("Lucas", 30),
        )
    connection.commit()
    print("Inserted customer")
