#rules for making a connection and binding
#ip,port, make socket object with TCP/UDP 
#bind it listen on the address
#connect it
#send or receive

import socket

tcps=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP='127.0.0.1'
PORT=6523
tcps.bind((IP,PORT))
tcps.listen(1)
#1 may be number of connections
#server done its role
conn,addr=tcps.accept()
print ('Connection Address is: ' , addr)
while True:
	data = conn.recv(200)     
	if not data:   
	    break 	
print("received data::::",data)
conn.send(data)
conn.close()
