from flask import Flask, render_template
import sqlite3
import db.config

DEVELOPMENT_ENV = True

app = Flask(__name__)

def executeSQL(db_filepath, sql_query, values=None):
    """Creates sqlite object and executes an SQL query

    Args:
        db_filepath (string): absolute filepath for the sqlite3 db
        sql_query (string): SQL query to execute

    Returns:
        sqlite3 cursor object
    """
    global connection # for use in other functions

    connection = sqlite3.connect(db_filepath)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(f"""{sql_query}""", values)
    
    return cursor

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/weight')
def weight_page():

    QUERY = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
    VALUES = () # simple query, no ETL

    cursor = executeSQL(db.config.DB_FILE_PATH, sql_query=QUERY, values=VALUES)
    rows = cursor.fetchall()

    labels = [row["date"] for row in rows]
    values = [row["weight"] for row in rows]

    ######################## data for Strength Chart HERE ########################

    QUERY = "SELECT date, exercise, SUM(reps * weight) from workouts GROUP BY date, exercise limit 5;"
    VALUES = ()

    ##############################################################################

    connection.commit()
    connection.close()

    return render_template('weight.html', labels=labels, values=values)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)

############################# End #############################

# @app.route('/progress')
# def progress_page():

#     items = [
#         {'id': 1, 'name': 'Weight'},
#         {'id': 2, 'name': 'Strength'},
#         {'id': 3, 'name': 'Cardio'}
#     ]

#     return render_template('progress.html', items=items)