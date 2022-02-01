from flask import Flask, render_template
import sqlite3
import db.config
import plotly.express as px

app = Flask(__name__)

DEVELOPMENT_ENV = True

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



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/progress')
def progress_page():
    items = [
        {'id': 1, 'name': 'Weight'},
        {'id': 2, 'name': 'Strength'},
        {'id': 3, 'name': 'Cardio'}
    ]
    return render_template('progress.html', items=items)

@app.route('/progress/weight')
def weight_page():

    QUERY = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
    VALUES = () # simple query, no ETL

    cursor = executeSQL(db.config.DB_FILE_PATH, sql_query=QUERY, values=VALUES)
    rows = cursor.fetchall()

    X = [row["date"] for row in rows]
    Y = [row["weight"] for row in rows]

    connection.commit()
    connection.close()

    fig = px.line(x=X, y=Y)
    # fig.show()

    data = {'Plot': fig.show()}

    return render_template('weight.html', items=data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)