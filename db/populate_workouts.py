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

# Imports the WorkoutExport file into the workouts table (run the following 3 lines in shell)

# (.fitness-app) md_ghsd@cloudshell:~/fitness-app/db (fitness-app-338622)$ sqlite3
# sqlite> .mode csv
# sqlite> .import c:/sqlite/city_no_header.csv cities

connection.commit()
