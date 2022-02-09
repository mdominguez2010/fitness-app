import sqlite3
from sqlite3 import Error
import config

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