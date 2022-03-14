import sqlite3
from sqlite3 import Error
import config

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

## ETL queries
# """
# CREATE TABLE IF NOT EXISTS weight (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     date TEXT NOT NULL,
#     weight TEXT NOT NULL,
#     fatmass TEXT,
#     bonemass TEXT,
#     musclemass TEXT,
#     hydration TEXT,
#     comments TEXT
# )
# """

# """
# CREATE TABLE IF NOT EXISTS workouts (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     date TEXT NOT NULL,
#     exercise TEXT NOT NULL,
#     reps TEXT NOT NULL,
#     weight TEXT NOT NULL,
#     duration TEXT NOT NULL,
#     distance TEXT NOT NULL,
#     incline TEXT NOT NULL,
#     resistance TEXT NOT NULL,
#     isWarmup TEXT NOT NULL,
#     note TEXT,
#     multiplier TEXT NOT NULL
# )
# """

db_file = config.DB_FILE_PATH

query = """
CREATE TABLE IF NOT EXISTS miles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    miles TEXT NOT NULL,
    duration_min TEXT NOT NULL,
    duration_sec TEXT NOT NULL,
    duration_total_ec TEXT NOT NULL,
    duration_total_min TEXT NOT NULL
)
"""

create_table(db_file=db_file, query=query)