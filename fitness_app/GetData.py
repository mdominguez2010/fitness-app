# from fitness_app import app_db, SQLAlchemy
# from fitness_app.db import config
# import datetime
# import sqlite3
# from sqlite3 import Error



# def executeSQL(db_filepath, sql_query, values=None):
#     """Creates sqlite object and executes an SQL query

#     Args:
#         db_filepath (string): absolute filepath for the sqlite3 db
#         sql_query (string): SQL query to execute

#     Returns:
#         sqlite3 cursor object
#     """
#     connection = None
    
#     try:
        
#         connection = sqlite3.connect(db_filepath)
#         connection.row_factory = sqlite3.Row
#         cursor = connection.cursor()
#         cursor.execute(f"""{sql_query}""", values)
        
#     except Error as e:
#         print(e)
        
#     return connection, cursor


# def get_data():
#     """
#     Returns the desired data from executeSQL function
#     """

#     tables = ["weight", "workouts", "runs"]
#     measurements = ["exericise_volume", "one_rep_max"]
#     exercises = ["Deadlift", "Back Squat", "Barbell Bench Press", "Pull Up"]
    
#     data_dict = dict()
    
#     for i in range(len(tables)):
        
#         if tables[i] == "weight":

#             # Daily weight

#             goal_weight = int(200)
#             query_weight = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
#             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_weight, values=None)
#             rows_weight = cursor.fetchall()

#             # Progress
            
#             query_progress = "SELECT ROUND((SELECT weight FROM weight WHERE date = (SELECT MAX(date) FROM weight)) - (SELECT weight FROM weight WHERE date(date) > '2021-12-31' ORDER BY date(date) ASC LIMIT 1), 1);"
#             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_progress, values=None)
#             rows_progress = cursor.fetchall()            

#             data_dict[tables[i]] = {
#                 "date": [x for x in range(len(rows_weight))],
#                 "daily_weight": [rows_weight["weight"] for row in rows_weight],
#                 "goal": goal_weight,
#                 "progress": rows_progress,
#                 "start_date": datetime.datetime.strptime("2022/01/01", "%Y/%m/%d")
#             }
            
#         elif tables[i] == "workouts":
            

#             for measurement in measurements:


#                     if measurement == "exercise_volume":


#                         for exercise in exercises:
                            
#                             # Exercise volume
#                             query_exercise_volume = f"SELECT exercise, SUM(reps * weight) as volume FROM workouts WHERE exercise = '{exercise}' GROUP BY date HAVING SUM(reps * weight) > 0 ORDER BY date ASC LIMIT 10;"
#                             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_exercise_volume, values=None)
#                             rows_exercise_volume = cursor.fetchall()

#                             data_dict[tables[i]][measurement]["date"] = [x for x in range(len(rows_exercise_volume))]
#                             data_dict[tables[i]][measurement][exercise] = [rows_exercise_volume["volume"] for row in rows_exercise_volume]                        

#                     else:

#                         for exercise in exercises:
                            
#                             # One-rep max
#                             query_one_rep_max = f"SELECT exercise, MAX((weight * 2.20462) * reps * .0333 + (weight * 2.20462)) as orm FROM workouts WHERE exercise = '{exercise}' LIMIT 10;"
#                             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_one_rep_max, values=None)
#                             rows_one_rep_max = cursor.fetchone()

#                             data_dict[tables[i]][measurement][exercise] = rows_one_rep_max

#         else:
            
#             # print(tables[i])

#             query_mile_time = "SELECT date, miles, duration_total_min FROM miles ORDER BY date ASC;"
#             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_mile_time, values=None)
#             rows_mile_times = cursor.fetchall()

#             query_fastest_mile = "SELECT MIN(duration_total_min) from miles;"
#             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_fastest_mile, values=None)
#             rows_fastest_mile = cursor.fetchone()


#             query_longest_run = "SELECT MAX(total_miles) FROM (SELECT date, SUM(miles) as total_miles FROM miles GROUP BY date ORDER BY date ASC) as longest_run;"
#             connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_longest_run, values=None)
#             rows_longest_run = cursor.fetchone()         
            
#             data_dict[tables[i]] = {
#                 "miles": {
#                     "date": [x for x in range(len(rows_mile_times))],
#                     "mile_time": [rows_mile_times["duration_total_min"] for row in rows_mile_times],
#                     "fastest_mile": rows_fastest_mile,
#                     "longest_run": rows_longest_run
#                 }
#             }
    
#     connection.commit()
#     connection.close()
    
#     for key in data_dict.keys():
#         print(key + "-->" + str(data_dict[key]) + "\n")

#     return data_dict

import datetime


tables = ["weight", "workouts", "runs"]
measurements = ["exercise_volume", "one_rep_max"]
exercises = ["Deadlift", "Back Squat", "Barbell Bench Press", "Pull Up"]

data_dict = {
    "weight": {
        "date": [],
        "daily_weight": [],
        "goal": 200,
        "progress": -25,
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

data_dict["weight"]["goal"] = 225.0

for key in data_dict.keys():
    print(key + "-->" + str(data_dict[key]) + "\n")
