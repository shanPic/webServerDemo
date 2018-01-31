from socket import *
severport = 12000
severSocket = socket(AF_INET,SOCK_DGRAM)
severSocket.bind(("",severport))
print("is ready ")
while 1:
    m , ad = severSocket.recvfrom(2048);
    severSocket.sendto("ok",ad);