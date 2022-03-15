import sqlite3
from sqlite3 import Error
import config
import csv
from drop_db import drop_tables
from create_db import create_table
import check_miles

if check_miles.UPDATE_MILES:

    try:

        FILENAME = "miles.csv"
        TABLENAME = "miles"

        DB_FILE = config.DB_FILE_PATH
        TABLES = ["miles"]
        QUERY = """
        CREATE TABLE IF NOT EXISTS miles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            miles TEXT NOT NULL,
            duration_min TEXT NOT NULL,
            duration_sec TEXT NOT NULL,
            duration_total_sec TEXT NOT NULL,
            duration_total_min TEXT NOT NULL
        )
        """

        # Drop the table first
        drop_tables(db_file=DB_FILE, tables_to_drop=TABLES[0])

        create_table(db_file=DB_FILE, query=QUERY)

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
        insert_records = f"INSERT INTO {TABLENAME} (date, distance, avg_pace_min, avg_pace_sec, duration_min, duration_sec, calories) VALUES (?, ?, ?, ?, ?, ?, ?)"

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

        # Close db connection
        connection.close()
            
    except Exception as e:
        print(e)
            