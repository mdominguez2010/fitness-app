import os
import datetime
import config

f = config.WOE_FILE_PATH
statbuf = os.stat(f)
mod_time = statbuf.st_mtime

timestamp_file = datetime.datetime.fromtimestamp(mod_time)

timestamp_today =  datetime.datetime.now()

time_elapsed = timestamp_today - timestamp_file

print("Modification time: {}".format(timestamp_file))
print("Current time: {}".format(timestamp_today))
print("Time elapsed: {}".format(time_elapsed))