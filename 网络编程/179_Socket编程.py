# '''
# socket：通过网络完成进程间的通信方式
# '''
from socket import *
# s=socket(AF_INET,SOCK_DGRAM)
# s.bind(('127.0.0.1',8788))
# addr=('127.0.0.1',8585)
# while True:
#     data = input("输入要发送的内容（输入 quit 退出）：")
#     if data.lower() == "quit":
#         print("退出程序")
#         break
#
#     # 发送
#     s.sendto(data.encode('gb2312'), addr)
#
#     # 接收（阻塞，直到收到数据）
#     redata, raddr = s.recvfrom(2048)
#     print("收到来自 {}:{} 的消息: {}".format(
#         raddr[0], raddr[1], redata.decode('gb2312'))
#     )
#
# s.close()


# from socket import *
#
# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('127.0.0.1', 8788))
#
# print("UDP 服务已启动，等待接收数据...")
#
# while True:
#     data, addr = s.recvfrom(2048)
#     print("来自 {}:{} 的消息: {}".format(addr[0], addr[1], data.decode('gb2312')))
#
#     # 可以选择回发
#     s.sendto(("已收到: " + data.decode('gb2312')).encode('gb2312'), addr)

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8788))
s.sendto(b'hello',('127.0.0.1',8585))
redata=s.recvfrom(1024)
print(redata[0].decode())