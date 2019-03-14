import os
import time
import sys

starttime = time.time()

while True:
    if time.time() >= starttime + 300:

	os.system('./dropbox_uploader.sh delete /dropbox/log_temp2.csv')
	os.system('./dropbox_uploader.sh upload log_temp2.csv /dropbox/')
	starttime = time.time()
