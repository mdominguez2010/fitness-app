"""
Determines if there's been a change in the source csv file.
If so, it's time to update our db
"""
import sqlite3
from sqlite3 import Error
import config
from csv import reader

UPDATE_MILES = False
QUERY = 'SELECT * FROM miles;'
FILENAME = config.M_FILE_PATH

def executeSQL(db_filepath, sql_query, values=None):
    """Creates sqlite object and executes an SQL query

    Args:
        db_filepath (string): absolute filepath for the sqlite3 db
        sql_query (string): SQL query to execute

    Returns:
        sqlite3 cursor object
    """
    connection = None
    
    try:
        
        connection = sqlite3.connect(db_filepath)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"""{sql_query}""", values)
        
    except Error as e:
        print(e)
        
    return connection, cursor



# Connect to Sqlite db
connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=QUERY, values=())

# Fetch our data
rows = cursor.fetchall()


db_rows = []
for row in rows:
    db_rows.append([x for x in row])
n_db_rows = len(db_rows)

# Count file rows
file_rows = []
with open(FILENAME, "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        file_rows.append(row)
n_file_rows = len(file_rows)

# User Feedback
print(f"# rows in file: {n_file_rows}")
print(f"# rows in db: {n_db_rows}")


# Check for new lines in the file
if n_file_rows > n_db_rows:
    UPDATE_MILES = True
    print("The file has changed. The db is being updated")
else:
    UPDATE_MILES
    print("Currently no changes to the file")
