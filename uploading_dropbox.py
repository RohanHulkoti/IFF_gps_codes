import os
import time
import sys

starttime = time.time()

while True:
    if time.time() >= starttime + 300:

	os.system('./dropbox_uploader.sh delete /drone_gps_backup/log_temp2.csv')
	os.system('./dropbox_uploader.sh upload log_temp2.csv /drone_gps_backup/')
	starttime = time.time()
