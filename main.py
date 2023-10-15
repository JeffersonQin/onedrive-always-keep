import os
import time


# Get the path and duration from the config
path = os.environ.get('ONEDRIVE_REFRESH_PATH')
duration = os.environ.get('ONEDRIVE_REFRESH_DURATION')

# Walk through the directory and open each file
while True:
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), 'rb') as f:
                f.read(1024)
    time.sleep(int(duration))
