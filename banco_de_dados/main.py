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
    # update
    with connection.cursor() as cursor:
        update = f"UPDATE {TABLE_NAME} SET age = 30 WHERE id = 1"
        result = cursor.execute(update)
        connection.commit()
        customers = cursor.fetchall()
        for customer in customers:
            print(customer)
