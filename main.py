from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
import db.config

DEVELOPMENT_ENV = True
app = Flask(__name__)

## Config (FOR TESTING ONLY)
# app.config["SERVER_NAME"] = "127.0.0.1:5000"

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


@app.route("/")
@app.route("/home")
def home_page():
    # with app.app_context():  # FOR TESTING ONLY
    return render_template("home.html")


@app.route("/weight")
def weight_page():

    QUERY = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
    VALUES = ()  # simple query, no ETL

    connection, cursor = executeSQL(
        db.config.DB_FILE_PATH, sql_query=QUERY, values=VALUES
    )
    rows = cursor.fetchall()

    labels = [row["date"] for row in rows]
    values = [row["weight"] for row in rows]

    connection.commit()
    connection.close()

    return render_template("weight.html", labels=labels, values=values)


@app.route("/strength")
def strength_page():

    QUERY = "SELECT substr(date, 1, 10) as date, exercise, reps, weight, SUM(reps*weight) AS TotalVolume, duration, distance FROM workouts GROUP BY substr(date, 1, 10) ORDER BY substr(date, 1, 10) ASC LIMIT 10;"
    VALUES = ()

    connection, cursor = executeSQL(
        db.config.DB_FILE_PATH, sql_query=QUERY, values=VALUES
    )
    rows = cursor.fetchall()

    labels_strength = [row["date"] for row in rows]
    values_strength = [row["TotalVolume"] for row in rows]

    connection.commit()
    connection.close()

    return render_template(
        "strength.html",
        labels_strength=labels_strength,
        values_strength=values_strength,
    )


@app.route("/cardio")
def cardio_page():

    # QUERY = ";"
    # VALUES = ()

    # connection, cursor = executeSQL(db.config.DB_FILE_PATH, sql_query=QUERY, values=VALUES)
    # rows = cursor.fetchall()

    # labels_cardio = [row["date"] for row in rows]
    # values_cardio = [row["TotalVolume"] for row in rows]

    # connection.commit()
    # connection.close()

    # return render_template("cardio.html", labels_=labels_cardio, values_=values_cardio)
    return render_template("cardio.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)
