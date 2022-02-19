import sqlite3
from sqlite3 import Error
import config
import csv
from drop_db import drop_tables
from create_db import create_table
import check_weight

if check_weight.UPDATE_WEIGHT:
    
    try:

        FILENAME = "weight.csv"
        TABLENAME = "weight"

        DB_FILE = config.DB_FILE_PATH
        TABLES = ["weight"]
        QUERY = """
        CREATE TABLE IF NOT EXISTS weight (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            weight TEXT NOT NULL,
            fatmass TEXT,
            bonemass TEXT,
            musclemass TEXT,
            hydration TEXT,
            comments TEXT
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

        # Commit changes
        connection.commit()

        # Close db connection
        connection.close()
    
    except:
        print("An exception has ocurred")