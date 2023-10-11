#socket programming: server and client connect with each other using port
import socket

#server socket:s
#creation of socket
s=socket.socket()
print('socket created')

#bind packet with server port number
s.bind(('localhost',9999))

#for three connection
s.listen(3)
print('waiting for connections')

while True:
    #accept connection from client
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("connected with",addr,name)

    #send in the form of byte
    c.send(bytes('welcome to telusko','utf-8'))

    c.close()