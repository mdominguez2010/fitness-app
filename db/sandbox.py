import os
import datetime
import config

f = config.WOE_FILE_PATH
statbuf = os.stat(f)
mod_time = statbuf.st_mtime

timestamp_file = datetime.datetime.fromtimestamp(mod_time)

timestamp_today =  datetime.datetime.now()

time_elapsed = timestamp_today - timestamp_file

print("\nModification time: {}".format(timestamp_file))
print("Current time: {}".format(timestamp_today))
print("Time elapsed: {}\n".format(time_elapsed))

if time_elapsed >= datetime.timedelta(days=1):
    print(">1 day has elapsed since the file was modified")
else:
    print("<1 days has elapsed since the file was modified")
    
def check_file_mod_time(abs_filepath):
    """[Checks how long ago the file was modified]

    Args:
        abs_filepath ([string]): [Absolute filepath of file]
    """
    
    return time_elapsed