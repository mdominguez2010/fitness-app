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


def get_data(connection, cursor):
    """
    Returns the desired data from executeSQL function
    """
    data_dict = dict()
    rows = cursor.fetchall()
    
    return data_dict


############## Final data object should look like this ##############
data_dict = {
    "weight_over_time": {
        "date": [1, 2, 3], 
        "daily weight": [200, 204, 206], # list of weights
        "Goal": 200,
        "Progress": -5,
        "progress since": "2022-01-01", # start date of goals       
    },
    "workouts": {
        "one_rep_max": {
            "date": [1, 2, 3], # tracked over time
            "Deadlift": [1, 2, 3],
            "Back Squat": [1, 2, 3],
            "Barbell Bench Press": [1, 2, 3],
            "Pull Up": [1, 2, 3]
        },
        "volume": {
            "Deadlift": 1000,
            "Back Squat": 2000,
            "Barbell Bench Press": 3000,
            "Pull Up": 10
        }
    },
    "runs": {
        "fastest mile": 9, # minutes
        "longest run": 5 # miles 
    }
}
