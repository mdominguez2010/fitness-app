import sqlite3
from sqlite3 import Error
import config
import pathlib
import csv

FILENAME = "WorkoutExport.csv"
TABLENAME = "workouts"

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
insert_records = f"INSERT INTO {TABLENAME} (date, exercise, reps, weight, duration, distance, incline, resistance, isWarmup, note, multiplier) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Importing contents of csv file into table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from the table to
# verify successful insertion
select_all = f"SELECT * FROM {TABLENAME}"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for row in rows[:5]:
    print(row)

# Commit changes
connection.commit()

# Close db connection
connection.close()









# import sqlite3
# from sqlite3 import Error
# import config
# import pathlib

# ## To update the workouts table with the current WorkoutExport file, run the following 3 lines in shell
# # (.fitness-app) md_ghsd@cloudshell:~/fitness-app/db (fitness-app-338622)$ sqlite3
# # sqlite> .mode csv
# # sqlite> .import c:/sqlite/city_no_header.csv cities

# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by the db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     connection = None
#     try:
#         connection = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)

#     return connection

# def select_all(table_name, connection, n_rows=10):
#     """
#     Query all rows in the table
#     :param conn: the Connection object
#     :return:
#     """
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM {table_name}")

#     rows = cursor.fetchall()

#     for row in rows[:n_rows]:
#         print(row)

# # Connect to database
# connection = create_connection(config.DB_FILE_PATH)

# # Select all objects in desired table
# TABLE_NAME = "workouts"
# select_all(table_name = TABLE_NAME,connection=connection, n_rows=2)

# # Close connection
# connection.commit()
# connection.close()