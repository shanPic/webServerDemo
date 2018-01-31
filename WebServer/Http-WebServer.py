#-*- coding: UTF-8-*-
#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) #类型为TCP套接字

#Prepare a sever socket
serverPort = 13333
serverSocket.bind( ('',serverPort) )
serverSocket.listen(1)
print("The server Socket is ready!")

while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#建立连接-->接收信息，建立了一个新的connectionSocket套接字，用于此用户
    try:
        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = ("HTTP/1.1 200 OK\nConnection: close\nContent-Length: %d\nContent-Type: text/html;charset=utf-8\n\n" % (len(outputdata))) #+ f
        connectionSocket.send(header)
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        header = ("HTTP/1.1 404 Found")
        connectionSocket.send(header.encode())
        #Close client socket
    connectionSocket.close();
serverSocket.close()
