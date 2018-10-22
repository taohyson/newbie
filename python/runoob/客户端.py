import socket

s = socket.socket() 
s.connect('106.75.227.42', 12345)
print s.recv()
s.close()