import sqlite3
from sqlite3 import Error
import config
import csv
# from drop_db import drop_tables
# from create_db import create_table
import check_miles


def drop_tables(db_file, tables_to_drop):
    """
    Create a database connection to the SQLite database
    specified by the db_file and drops the specified tables
    
    :param db_file: database filepath (string)
    :param tables_to_drop: list-like (list of strings)
    
    :return: None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
    except Error as e:
        print(e)
        
    for table in tables_to_drop:
        cursor.execute(f"""
            DROP TABLE IF EXISTS {table};
        """)

    connection.commit()
    connection.close()


def create_table(db_file, query):
    """
    Create a database connection to the SQLite database
    specified by the db_file and creates specified table
    
    :param db_file: database filepath (string)
    :param tables_to_drop: list-like (list of strings)
    
    :return: None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
    except Error as e:
        print(e)
        
    cursor.execute(f"""
        {query};
    """)

    connection.commit()


##### Remove header columns names from miles.csv file before proceeding


if check_miles.UPDATE_MILES:

    try:

        FILENAME = "miles.csv"
        TABLENAME = "miles"

        DB_FILE = config.DB_FILE_PATH
        TABLES = ["miles"]
        QUERY_create_table = """
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

        create_table(db_file=DB_FILE, query=QUERY_create_table)

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
        for row in rows[-5:]:
            print(row)

        # Close db connection
        connection.close()
            
    except Exception as e:
        print(e)
            