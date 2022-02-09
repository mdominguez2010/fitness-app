import pathlib

## Get absolute paths
# app db
DB_FILE_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/app.db"

# WorkoutExport
WOE_FILE_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/WorkoutExport.csv"

# weight
WEE_FILE_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/weight.csv"

# populate_workouts
WO_FILE_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/populate_workouts.py"

# populate_weight
WE_FILE_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/populate_weight.py"

# print(DB_FILE_PATH)