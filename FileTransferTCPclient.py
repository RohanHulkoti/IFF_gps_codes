import socket

s = socket.socket()
host = "10.8.0.10"
port = 4161

s.connect((host,port))
s.send("Hello Server!")

with open('log_temp2.csv',"wb") as f:

    print'file opened'

    while True:
	data = s.recv(1024)
	if not data:
	    break
	print((data))
	f.write(data)
#	sys.stdout.flush()

f.close()
s.close()
