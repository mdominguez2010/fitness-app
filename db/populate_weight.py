import sqlite3
from sqlite3 import Error
import config
from remove_header_from_csv import remove_header_from_csv
import pathlib
import csv


TABLENAME = "weight"

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
connection = create_connection(config.DB_FILE_PATH)

# Create cursor object
cursor = connection.cursor()

# Open the csv file
file = open(FILENAME)

# Reading contents of file
contents = csv.reader(file)

# SQL query to execute
insert_records = f"INSERT INTO {TABLENAME} (date, weight, fatmass, bonemass, musclemass, hydration, comments) VALUES (?, ?, ?, ?, ?, ?, ?)"

# Importing contents of csv file into table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from the table to
# verify successful insertion
select_all = "SELECT * FROM weight"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for row in rows[:5]:
    print(row)

# Commit changes
connection.commit()

# Close db connection
connection.close()