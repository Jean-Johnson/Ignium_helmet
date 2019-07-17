import socket 
import time
import Adafruit_ADS1x15
import pulsedetect
host = '192.168.43.5'
port = 4000
start=0
s=socket.socket()
def check():
	varp=pulsedetect.detect()
	if varp>0:
		data="pulse detected"
	else:
		data="nothing"
	return data
def transmit():
	s.connect((host,port))
	status=check()
	while status=="nothing":
		status=check()
	if status=="pulse detected":
		print("var"+status)
		s.send(status.encode('utf-8'))
		data=s.recv(1024).decode('utf-8')
		if data=="started":
			 start=1
		while start==1:
			time.sleep(2)
			status=check()
			print(status)
			s.send(status.encode('utf-8'))

if __name__=='__main__':
	transmit()
