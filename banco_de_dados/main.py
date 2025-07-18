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
        sql = (f"INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)")
        data2 = (
            ("Lauro", 30),
            ("Maria", 25),
            ("João", 40),
            ("Ana", 35),
            ("Pedro", 28),
            ("Carla", 32),
            ("Rafael", 29),
            ("Fernanda", 31),
            ("Roberto", 45),
            ("Patrícia", 27),
        )
        result = cursor.executemany(sql, data2)
        connection.commit()
    print("Inserted customer")
# select
    with connection.cursor() as cursor:
        select = (f"SELECT * FROM {TABLE_NAME} WHERE age > 25")
        result = cursor.execute(select)
        customers = cursor.fetchall()
        for customer in customers:
            print(customer)