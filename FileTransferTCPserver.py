import time
import socket

port = 4161
s = socket.socket()
host = "10.8.0.10"

s.bind((host,port))
s.listen(5)

print 'Server listening....'

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    try:
	filename = 'log_temp.csv'
        f = open(filename,'rb')
        l = f.read(117)
        f.close()
        while True:
            conn.send(l)
            time.sleep(1)
            f = open(filename,'rb')
	    l = f.read(117)

    except (socket.error), e:
	conn.close()
	print e.args, e.message
	print 'Server again listening....'
#	conn.send(l)
#	time.sleep(1)
#	l.read(117)
#    f.close()
#    filename = 'log_temp.txt'
#    f = open(filename,'rb')
#    l = f.read(117)
#    l.read(117)
    #f.close()
conn.close()
