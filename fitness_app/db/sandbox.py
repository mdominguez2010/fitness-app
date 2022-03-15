from create_db import create_table
import sqlite3
from sqlite3 import Error
import config
import csv

########## Params ##########

DB_FILE = config.DB_FILE_PATH
FILENAME = "miles.csv"
TABLENAME = "miles"

############################


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
insert_records = f"INSERT INTO {TABLENAME} (date, miles, duration_min, duration_sec, duration_total_sec, duration_total_min) VALUES (?, ?, ?, ?, ?, ?)"

# Importing contents of csv file into table
cursor.executemany(insert_records, contents)

# Commit changes
connection.commit()

# SQL query to retrieve all data from the table to
# verify successful insertion
select_all = f"SELECT * FROM {TABLENAME}"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for row in rows[:5]:
    print(row)
