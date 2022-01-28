import sqlite3
import config

# Connect to database
connection = sqlite3.connect(config.DB_FILE_PATH)

# Create cursor object
cursor = connection.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weight (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        weight REAL NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        exercise TEXT NOT NULL,
        reps INTEGER NOT NULL,
        weight REAL NOT NULL,
        duration REAL NOT NULL,
        distance REAL NOT NULL,
        incline REAL NOT NULL,
        resistance REAL NOT NULL,
        isWarmup NOT NULL,
        note TEXT,
        multiplier INTEGER NOT NULL
    )
""")

connection.commit()



###########################################################

# CREATE TABLE IF NOT EXISTS weight(
#   id INT PRIMARY KEY     NOT NULL,
#   date           TEXT    NOT NULL,
#   weight            REAL     NOT NULL
# );