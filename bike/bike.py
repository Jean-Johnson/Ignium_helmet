import socket
import time
from gpiozero import LED

init=0
start=0
host='192.168.43.5'
port=4000
led=LED(17)
s=socket.socket()
def ignite():
	global start
	global init
	start=1
	init=1
	led.on()
	time.sleep(4)
	print("[+]bike moving")
def kill():
	global start
	start=0
	led.off()
	print("varkilled")
	print("[-]Bike stopped")
	exit()
def reciver():
	s.bind((host,port))
	s.listen(1)
	obj, addr=s.accept()
	print("connected only")
	while init==0 and start==0:
		data=obj.recv(1024).decode('utf-8')
		if data=="pulse detected":
			ignite()
			data="started"
			obj.send(data.encode('utf-8'))
			break
	print(init)
	while init==1:
		data=obj.recv(1024).decode('utf-8')
		time.sleep(2)
		if data!="pulse detected":
			print("inside no pulse"+data)
			time.sleep(2)
			data=obj.recv(1024).decode('utf-8')
			if data=="nothing":
				kill()
if __name__=='__main__':
	reciver()
