import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind('0.0.0.0',port)

s.listen(5)
while True:
	c, addr = s.accept()
	print addr
	c.send("Welcome to my server")
	c.close()
