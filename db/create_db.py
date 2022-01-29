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
        id INTEGER PRIMARY KEY
        date TEXT NOT NULL,
        exercise TEXT NOT NULL,
        reps TEXT NOT NULL,
        weight TEXT NOT NULL,
        duration TEXT NOT NULL,
        distance TEXT NOT NULL,
        incline TEXT NOT NULL,
        resistance TEXT NOT NULL,
        isWarmup TEXT NOT NULL,
        note TEXT,
        multiplier TEXT NOT NULL
    )
""")

connection.commit()
connection.close()


###########################################################

# CREATE TABLE IF NOT EXISTS weight(
#   id INT PRIMARY KEY     NOT NULL,
#   date           TEXT    NOT NULL,
#   weight            REAL     NOT NULL
# );