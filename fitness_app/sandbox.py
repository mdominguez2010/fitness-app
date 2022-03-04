import datetime
import sqlite3
from sqlite3 import Error



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
            
            data_dict[tables[i]] = {
                "one_rep_max": {
                    "date": [1, 2, 3],
                    "Deadlift": [1, 2, 3],
                    "Back Squat": [1, 2, 3],
                    "Barbell Bench Press": [1, 2, 3],
                    "Pull Up": [1, 2, 3]
                },
                "max_volume": {
                    "Deadlift": 1000,
                    "Back Squat": 2000,
                    "Barbell Bench Press": 3000,
                    "Pull Up": 10                    
                }                    
            }

        else:
            
            # print(tables[i])

            query = ""
            
            data_dict[tables[i]] = {
                "runs": {
                    "date": [1, 2, 3],
                    "mile_time": [9, 10, 11],
                    "fastest_mile": int(),
                    "longest_run": int()
                }
            }

    # connection.commit()
    # connection.close()
    
    print(data_dict)

    return data_dict

get_data()
