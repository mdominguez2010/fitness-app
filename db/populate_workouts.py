import sqlite3
from sqlite3 import Error
import config
import pathlib

## To update the workouts table with the current WorkoutExport file, run the following 3 lines in shell
# (.fitness-app) md_ghsd@cloudshell:~/fitness-app/db (fitness-app-338622)$ sqlite3
# sqlite> .mode csv
# sqlite> .import c:/sqlite/city_no_header.csv cities

def create_connection(db_file):
    """ create a database connection to the SQLite database
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

def select_all(connection, n_rows=10):
    """
    Query all rows in the table
    :param conn: the Connection object
    :return:
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM workouts")

    rows = cursor.fetchall()

    for row in rows[:n_rows]:
        print(row)

# Connect to database
connection = create_connection(config.DB_FILE_PATH)

# Select all objects in desired table
select_all(connection=connection, n_rows=2)

# Close connection
# connection.commit()
connection.close()