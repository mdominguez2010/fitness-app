import sqlite3
import config

# Connect to database
connection = sqlite3.connect(config.DB_FILE_PATH)

# Create cursor object
cursor = connection.cursor()

# Execute SQL commands

# Create database
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weight (
        id INTEGER PRIMARY KEY,
        date REAL NOT NULL,
        weight REAL NOT NULL
    )
""")

connection.commit()