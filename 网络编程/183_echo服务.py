from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('127.0.0.1', 8585))
while True:
    recvData = udpSocket.recv(1024)
    print(recvData[0].decode())
    data=input('请输入：')
    udpSocket.sendto(data.encode(),recvData[1])
udpSocket.close()
