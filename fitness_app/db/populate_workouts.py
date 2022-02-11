import sqlite3
from sqlite3 import Error
import os
import datetime
import config
import csv
from csv import reader
from drop_db import drop_tables
from create_db import create_table

FILENAME = "WorkoutExport.csv"
TABLENAME = "workouts"

DB_FILE = config.DB_FILE_PATH
TABLES = ["workouts"]
QUERY = """
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
"""

# Drop the table first
drop_tables(db_file=DB_FILE, tables_to_drop=TABLES)

def remove_header_from_csv(filename):
    """
    Removes first row from csv file
    """
    # Open csv file
    file = open(FILENAME)
    csvreader = csv.reader(file)

    # Extract data
    rows = []
    for row in csvreader:
        rows.append(row)
    # header = rows[0]
    data = rows[1:]

    # Close file
    file.close()

    # Write the rows data into the file
    with open(FILENAME, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    # Confirm written file
    # file = open(FILENAME)
    # csvreader = csv.reader(file)
    # rows = []
    # for row in csvreader:
    #     rows.append(row)

    # print(rows[:10])

    file.close()

create_table(db_file=DB_FILE, query=QUERY)

# First remove header from csv file
remove_header_from_csv(filename=FILENAME)

def create_connection(db_file):
    """
    create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection

# Connect to Sqlite db
connection = create_connection(DB_FILE)

# Create cursor object
cursor = connection.cursor()

# Open the csv file
file = open(FILENAME)

# Reading contents of file
contents = csv.reader(file)

# SQL query to execute
insert_records = f"INSERT INTO {TABLENAME} (date, exercise, reps, weight, duration, distance, incline, resistance, isWarmup, note, multiplier) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Importing contents of csv file into table
cursor.executemany(insert_records, contents)

# Commit changes
connection.commit()

# SQL query to retrieve all data from the table to
# verify successful insertion
select_all = f"SELECT * FROM {TABLENAME}"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for row in rows[-5:]:
    print(row)