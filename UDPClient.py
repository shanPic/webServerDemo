from socket import *
# from sys import *
SeverName = '67.209.179.53'
SeverHost = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM) #AF_INET 指示了底层网络使用的是IPv4. SOCK_DGRAM意味着它是一个UDP套接字
cnt = 0
while True:
    message = input("input message\n")
    clientSocket.sendto(message.encode(),(SeverName,SeverHost)) #需要将字符串对象转化为字节流（利用encode()方法）
    modim , adde = clientSocket.recvfrom(2048)      #当一个来自因特网的分组到达该客户套接字时，该分组的数据
    print(modim.decode('utf-8'))            #
    # sys.stdout.write(modim)
    if cnt == 2:
        break
clientSocket.close()