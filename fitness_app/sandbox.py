import datetime
import sqlite3
from sqlite3 import Error
from fitness_app.db import config


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


def get_data():
    """
    Returns the desired data from executeSQL function
    """

    tables = ["weight", "workouts", "runs"]
    measurements = ["one_rep_max", "max_volume"]
    exercises = ["Deadlift", "Back Squat", "Barbell Bench Press", "Pull Up"]
    
    data_dict = dict()
    
    for i in range(len(tables)):
        
        if tables[i] == "weight":

            # print(tables[i])
            
            # query = "SELECT date(date) as date, MIN(weight) as weight FROM weight WHERE date(date) > '2020-12-31' GROUP BY date ORDER BY date ASC;"
            # values = ()
            
            # connection, cursor = executeSQL(
            #     config.DB_FILE_PATH, sql_query=query, values=values
            # )
            
            # rows = cursor.fetchall()
            data_dict[tables[i]] = {
                "date": datetime.datetime.strptime("2022/03/04", "%Y/%m/%d"),
                "daily_weight": 250,
                "goal": int(210),
                "progress": int(-5),
                "start_date": datetime.datetime.strptime("2022/01/01", "%Y/%m/%d")
            }
            
        elif tables[i] == "workouts":
            
            # print(tables[i])

            query = ""

            for measurement in measurements:

                    # print(exercise)
                    # Build one_rep_max data

                    for exercise in exercises:
                        
                        data_dict[tables[i]][measurement]["date"] = datetime.datetime.strptime("2022/03/04", "%Y/%m/%d")
                        data_dict[tables[i]][measurement][exercise] = 1
                    
                        # data_dict[tables[i]] = {
                        #     "one_rep_max": {
                        #         "date": [1, 2, 3],
                        #         "Deadlift": [1, 2, 3],
                        #         "Back Squat": [1, 2, 3],
                        #         "Barbell Bench Press": [1, 2, 3],
                        #         "Pull Up": [1, 2, 3]
                        #     },
                        #     "max_volume": {
                        #         "Deadlift": 1000,
                        #         "Back Squat": 2000,
                        #         "Barbell Bench Press": 3000,
                        #         "Pull Up": 10                    
                        #     }                    
                        # }

        else:
            
            # print(tables[i])

            query_mile_time = "SELECT date, miles, duration_total_min FROM miles ORDER BY date ASC;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_mile_time, values=None)
            rows_mile_times = cursor.fetchall()

            query_fastest_mile = "SELECT MIN(duration_total_min) from miles;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_fastest_mile, values=None)
            rows_fastest_mile = cursor.fetchone()


            query_longest_run = "SELECT MAX(total_miles) FROM (SELECT date, SUM(miles) as total_miles FROM miles GROUP BY date ORDER BY date ASC) as longest_run;"
            connection, cursor = executeSQL(config.DB_FILE_PATH, sql_query=query_longest_run, values=None)
            rows_longest_run = cursor.fetchone()         
            
            data_dict[tables[i]] = {
                "miles": {
                    "date": [x for x in range(len(rows_mile_times))],
                    "mile_time": [rows_mile_times["duration_total_min"] for row in rows_mile_times],
                    "fastest_mile": rows_fastest_mile,
                    "longest_run": rows_longest_run
                }
            }
    

    connection.commit()
    connection.close()
    
    for key in data_dict.keys():
        print(key + "-->" + str(data_dict[key]) + "\n")

    return data_dict

get_data()
