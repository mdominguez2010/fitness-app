import sqlite3
import config

def create_connection(db_file):
    """
    create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database filepath
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection

# Establish connection to db
connection = create_connection(config.DB_FILE_PATH)
cursor = connection.cursor()

# Drop table(s)
TABLES = ["weight", "workouts"]
for table in TABLES:
    cursor.execute(f"""
        DROP TABLE {table}
    """)

connection.commit()
connection.close()