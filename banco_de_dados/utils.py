import sqlite3
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
DB_NAME = "sqlite.db"
DB_FILE = ROOT_FOLDER / DB_NAME
TABLE_NAME = "customers"
