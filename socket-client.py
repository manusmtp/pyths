import socket


IP='127.0.0.1'
clisock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT=6523

clisock.connect((IP,PORT))
clisock.sendall(b'test srever')
data=clisock.recv(200)
clisock.close()