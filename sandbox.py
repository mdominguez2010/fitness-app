import sqlite3
import db.config
import plotly.express as px
import pandas as pd

def executeSQL(db_filepath, sql_query, values=None):
    """Creates sqlite object and executes an SQL query

    Args:
        db_filepath (string): absolute filepath for the sqlite3 db
        sql_query (string): SQL query to execute

    Returns:
        sqlite3 cursor object
    """
    global connection

    connection = sqlite3.connect(db_filepath)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""{sql_query}""", values)
    
    return cursor

QUERY = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
VALUES = () # simple query, no ETL

cursor = executeSQL(db.config.DB_FILE_PATH, sql_query=QUERY, values=VALUES)
rows = cursor.fetchall()

# for row in rows:
#     print(row["date"], row["weight"])

X = [row["date"] for row in rows]
Y = [row["weight"] for row in rows]

df = pd.DataFrame({'Date': X, 'Weight': Y})

connection.commit()
connection.close()

# print(X[:5])
# print(Y[:5])

# print(type(X[0]))
# print(type(Y[0]))

fig = px.line(df, x="Date", y="Weight")
fig.show()