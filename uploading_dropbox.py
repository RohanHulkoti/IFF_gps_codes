import os
import time
import sys

starttime = time.time()

while True:
    if time.time() >= starttime + 300:

	os.system('./dropbox_uploader.sh delete /Drone_gps_backup/log_temp2.csv')
	os.system('./dropbox_uploader.sh upload log_temp2.csv /Drone_gps_backup/')
	starttime = time.time()
