import os
import datetime
import config

def check_file_mod_time(abs_filepath):
    """[Checks how long ago the file was modified]

    Args:
        abs_filepath ([string]): [Absolute filepath of file]
    """
    
    statbuf = os.stat(f)
    mod_time = statbuf.st_mtime
    timestamp_file = datetime.datetime.fromtimestamp(mod_time)
    timestamp_today =  datetime.datetime.now()
    time_elapsed = timestamp_today - timestamp_file
    
    return time_elapsed

def time_to_update(timedelta):
    """[Returns True if >= 1 day has elapsed, False if otherwise. If True, then it's time to update file]

    Args:
        timedelta ([timedelta]): [Time elapsed since last modified]
    """
    
    if time_elapsed >= datetime.timedelta(days=1):
        print(">1 day has elapsed since the file was modified")
        return False
    else:
        print("The file has been modified recently, let's update our database!")
        return True

f = config.WOE_FILE_PATH
time_elapsed = check_file_mod_time(f)


if time_to_update(time_elapsed):
    print("")

# print("\nModification time: {}".format(timestamp_file))
# print("Current time: {}".format(timestamp_today))
# print("Time elapsed: {}\n".format(time_elapsed))