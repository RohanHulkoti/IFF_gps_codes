#!/usr/bin/env python
import ublox
import sys
import socket
import datetime
import time
import os

LOG_FILE = "log" + datetime.datetime.now().isoformat() + ".ubx"
#TCP_IP = '0.0.0.0'
#TCP_PORT = 4161

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)

#starttime=time.time()


#print('Listening on {}:{}'.format(TCP_IP, TCP_PORT))

dev = ublox.UBlox("/dev/ttyS1")
dev.set_logfile(LOG_FILE)
#dev1.configure_message_rate(ublox.CLASS_NAV, ublox.MSG_NAV_POSLLH, 1)
file2 = open("log_temp2.csv","w")
while True:
 #   conn, addr = s.accept()
    msg = dev.receive_message(ignore_eof=True)
    if msg is None:
        "No Message."
        break
    if msg.name() == "NAV_POSLLH":
	print(str(msg)) # The numbers were counted and written. better would be to compare strings and concatenate-RSH
	file = open("log_temp.csv","w")
	file.write(str(msg)[17:26]+","+str(msg)[38:47]+","+str(msg)[58:67]+"\n")
	file2.write(str(msg)[17:26]+","+str(msg)[38:47]+","+str(msg)[58:67]+"\n")
	file.close()
#    if time.time() >= starttime + 10:
#	print(str(time.time()))
#	os.system('./dropbox_uploader.sh delete /dropbox/log_temp2.csv')
#	os.system('./dropbox_uploader.sh upload log_temp2.csv /dropbox')
#	starttime = time.time()
  #      conn.send(str(msg))
  #      print(type(msg.Longitude))
  #      print(float(msg.Longitude) / 10000000)
    sys.stdout.flush()
file.close()
conn.close()

