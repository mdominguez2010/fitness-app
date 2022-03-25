from fitness_app import app
from fitness_app.db import config
import sqlite3
from sqlite3 import Error
from flask import render_template
import datetime



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

################################### IN PROGRESS ###################################

def get_data():
    """
    Returns the desired data from executeSQL function
    """

    tables = ["weight", "workouts", "miles"]
    measurements = ["exercise_volume", "one_rep_max"]
    exercises = ["Deadlift", "Back Squat", "Barbell Bench Press", "Pull Up"]
    
    data_dict = {
    "weight": {
        "date": [],
        "daily_weight": [],
        "goal": 200,
        "progress": float(),
        "start_date": datetime.datetime.strptime("2022/01/01", "%Y/%m/%d")
    },
    "workouts": {
        "measurements": {
            "exercise_volume": {
                "dates": [],
                "Deadlift": [],
                "Back Squat": [],
                "Barbell Bench Press": [],
                "Pull Up":[]
            },
            "one_rep_max": {
                "Deadlift": 1,
                "Back Squat": 1,
                "Barbell Bench Press": 1,
                "Pull Up": 1
            }
        }
    },
    "miles": {
        "dates": [],
        "mile_time": [],
        "fastest_mile": 1,
        "longest_run": 1
        }
    }

    
    for table in tables:
        
        if table == "weight":

            # Daily weight

            query_weight = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_weight, values=())
            rows_weight = cursor.fetchall()

            data_dict[table]["date"] = [x for x in range(len(rows_weight))]
            data_dict[table]["daily_weight"] = rows_weight

            # Progress
            
            query_progress = "SELECT ROUND((SELECT weight FROM weight WHERE date = (SELECT MAX(date) FROM weight)) - (SELECT weight FROM weight WHERE date(date) > '2021-12-31' ORDER BY date(date) ASC LIMIT 1), 1);"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_progress, values=())
            rows_progress = cursor.fetchone()        

            data_dict[table]["progress"] = rows_progress
            data_dict[table]["start_date"] = datetime.datetime.strptime("2022/01/01", "%Y/%m/%d")

            
        elif table == "workouts":
            

            for measurement in measurements:


                    if measurement == "exercise_volume":


                        for exercise in exercises:
                            
                            # Exercise volume
                            query_exercise_volume = f"SELECT exercise, SUM(reps * weight) as volume FROM workouts WHERE exercise = '{exercise}' GROUP BY date HAVING SUM(reps * weight) > 0 ORDER BY date ASC;"
                            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_exercise_volume, values=())
                            rows_exercise_volume = cursor.fetchall()
                            data_dict[table]["measurements"][measurement]["dates"] = [x for x in range(len(rows_exercise_volume))]
                            data_dict[table]["measurements"][measurement][exercise] = rows_exercise_volume

                            # data_dict[tables[i]][measurements[i]]["date"] = [x for x in range(len(rows_exercise_volume))]
                            # data_dict[tables[i]][measurements[i]][exercises[i]] = [rows_exercise_volume[1] for row in rows_exercise_volume]                        

                    else:

                        for exercise in exercises:
                            
                            # One-rep max
                            query_one_rep_max = f"SELECT exercise, MAX((weight * 2.20462) * reps * .0333 + (weight * 2.20462)) as orm FROM workouts WHERE exercise = '{exercise}' LIMIT 10;"
                            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_one_rep_max, values=())
                            rows_one_rep_max = cursor.fetchone()

                            data_dict[table]["measurements"][measurement][exercise] = rows_one_rep_max

        else:
            

            query_mile_time = "SELECT date, miles, duration_total_min FROM miles ORDER BY date ASC;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_mile_time, values=())
            rows_mile_times = cursor.fetchall()

            query_fastest_mile = "SELECT MIN(duration_total_min) from miles;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_fastest_mile, values=())
            rows_fastest_mile = cursor.fetchone()


            query_longest_run = "SELECT MAX(total_miles) FROM (SELECT date, SUM(miles) as total_miles FROM miles GROUP BY date ORDER BY date ASC) as longest_run;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_longest_run, values=())
            rows_longest_run = cursor.fetchone()         
            
            data_dict[table]["dates"] = [x for x in range(len(rows_mile_times))]
            data_dict[table]["mile_time"] = rows_mile_times
            data_dict[table]["fastest_mile"] = rows_fastest_mile
            data_dict[table]["longest_run"] = rows_longest_run

    
    connection.commit()
    connection.close()
    
    # for key in data_dict.keys():
    #     print(key + "-->" + str(data_dict[key]) + "\n")

    return data_dict

################################### IN PROGRESS ###################################

@app.route("/")
@app.route("/home")
def home_page():
    # with app.app_context():  # FOR TESTING ONLY
    return render_template("home.html")


@app.route("/dashboard")
def dashboard_page():

    data_dict = get_data()

    # weight
    
    weights = data_dict["weight"]["daily_weight"]
    dates_list = []
    weights_list = []
    
    for weight in weights:
        dates_list.append(weight[0])
        weights_list.append(weight[1])

    progress = data_dict["weight"]["progress"]
        
    # workouts
    
    exercise_volume_deadlift = data_dict["workouts"]["measurements"]["exercise_volume"]["Deadlift"]
    orm = data_dict["workouts"]["measurements"]["one_rep_max"]["Deadlift"]

    # miles

    mile_times = data_dict["miles"]["mile_time"]
    mile_dates_list = []
    mile_times_list = []
    for mile_time in mile_times:
        mile_dates_list.append(mile_time[0])
        mile_times_list.append(mile_time[2])


    
    
    fastest_mile = data_dict["miles"]["fastest_mile"]
    longest_run = data_dict["miles"]["longest_run"]
    

    return render_template("dashboard.html", data_dict = data_dict, weights_list = weights_list, dates_list=dates_list, mile_times_list = mile_times_list, mile_dates_list=mile_dates_list, progress = progress, orm = orm, fastest_mile=fastest_mile, longest_run=longest_run)
