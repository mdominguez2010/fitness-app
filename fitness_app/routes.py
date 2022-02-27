from fitness_app import app
from fitness_app.db import config
import sqlite3
from sqlite3 import Error
from flask import render_template


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
        config.DB_FILE_PATH, sql_query=QUERY, values=VALUES
    )
    rows = cursor.fetchall()

    labels = [row["date"] for row in rows]
    values = [row["weight"] for row in rows]

    connection.commit()
    connection.close()

    return render_template("weight.html", labels=labels, values=values)


@app.route("/strength")
def strength_page():

    QUERY = "SELECT substr(date, 1, 10) as date, exercise, reps, weight, SUM(reps*weight) AS TotalVolume, duration, distance FROM workouts GROUP BY substr(date, 1, 10) HAVING SUM(reps*weight) > 0 ORDER BY substr(date, 1, 10) ASC;"
    VALUES = ()

    connection, cursor = executeSQL(
        config.DB_FILE_PATH, sql_query=QUERY, values=VALUES
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

    QUERY = "SELECT * FROM runs;"
    VALUES = ()

    connection, cursor = executeSQL(
        config.DB_FILE_PATH, sql_query=QUERY, values=VALUES
    )
    rows = cursor.fetchall()

    labels_cardio = [row["date"] for row in rows]
    values_cardio = [row["distance"] for row in rows]
    
    backgroundColors = ['rgba(54, 162, 235, 0.5)' for label in labels_cardio]
    borderColors= ['rgb(54, 162, 235, 1)' for label in labels_cardio]

    connection.commit()
    connection.close()  

    return render_template("cardio.html", labels_cardio=labels_cardio, values_cardio=values_cardio, backgroundColors=backgroundColors, borderColors=borderColors)

@app.route("/dashboard")
def dashboard_page():
    ###### WEIGHT ########
    QUERY_WEIGHT = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
    VALUES = ()  # simple query, no ETL

    connection, cursor = executeSQL(
        config.DB_FILE_PATH, sql_query=QUERY_WEIGHT, values=VALUES
    )
    rows = cursor.fetchall()

    labels_weight = [row["date"] for row in rows]
    values_weight = [row["weight"] for row in rows]
    
    ###### STRENGTH ########
    QUERY_STRENGTH = "SELECT substr(date, 1, 10) as date, exercise, reps, weight, SUM(reps*weight*2.2) AS TotalVolume, duration, distance FROM workouts GROUP BY substr(date, 1, 10) HAVING SUM(reps*weight) > 0 ORDER BY substr(date, 1, 10) ASC;"
    EXERCISE = ['Deadlift', 'Back Squat', 'Barbell Bench Press', 'Pull Up']
    QUERY_ONERM = f"SELECT exercise, MAX(weight*2.205) * (1 + (reps/30)) as one_rm FROM workouts WHERE exercise={EXERCISE[0]} GROUP BY exercise;"
    
    connection, cursor = executeSQL(
        config.DB_FILE_PATH, sql_query=QUERY_STRENGTH, values=VALUES
    )
    
    rows = cursor.fetchall()
    
    labels_strength = [row["date"] for row in rows]
    values_strength = [row["TotalVolume"] for row in rows]
    
    ###### Cardio ########
    QUERY_CARDIO = "SELECT * FROM runs;"
    connection, cursor = executeSQL(
        config.DB_FILE_PATH, sql_query=QUERY_CARDIO, values=VALUES
    )
    rows = cursor.fetchall()

    labels_cardio = [row["date"] for row in rows]
    values_cardio = [row["distance"] for row in rows]
    
    backgroundColors = ['rgba(54, 162, 235, 0.5)' for label in labels_cardio]
    borderColors= ['rgb(54, 162, 235, 1)' for label in labels_cardio]

    connection.commit()
    connection.close()

    return render_template("dashboard.html", labels_weight=labels_weight, values_weight=values_weight, labels_strength=labels_strength, values_strength=values_strength, labels_cardio=labels_cardio, values_cardio=values_cardio, backgroundColors=backgroundColors, borderColors=borderColors)
