import os
import time

# The path to the directory you want to clean up
directory = '/tmp'

# The file extension you're targeting
extension = '.jpg'

# How many seconds in 2 days (2 days * 24 hours/day * 60 minutes/hour * 60 seconds/minute)
age_threshold = 2 * 24 * 60 * 60

# Current time
now = time.time()

# Walk through the directory
for filename in os.listdir(directory):
    if filename.endswith(extension):
        file_path = os.path.join(directory, filename)
        # Get the file's modification time
        file_mod_time = os.path.getmtime(file_path)
        # If the file is older than the threshold, delete it
        if now - file_mod_time > age_threshold:
            os.remove(file_path)
            print(f"Deleted {file_path}")

print("Cleanup complete.")
