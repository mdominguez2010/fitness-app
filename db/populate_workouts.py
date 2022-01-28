import sqlite3
import config
import pathlib

# Connect to database
connection = sqlite3.connect(config.DB_FILE_PATH)

# Create cursor object
cursor = connection.cursor()

# Drop workouts table
cursor.execute("""
    DROP TABLE IF EXISTS workouts
""")

# Re-create table
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

# Imports the WorkoutExport file into the workouts table
cursor.execute("""
    .mode csv
""")

filename = "WorkoutExport.csv"
tablename = "workouts"
filepath = str(pathlib.Path(__file__).parent.resolve()) + filename

cursor.execute(f"""
    .import {filepath} {tablename}
""")

connection.commit()
