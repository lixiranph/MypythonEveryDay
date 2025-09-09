# -*- coding: gb2312 -*-
import threading
from socket import *

# === 配置 ===
LOCAL_BIND = ("0.0.0.0", 8089)      # 本机监听端口（与服务端错开）
PEER_ADDR  = ("127.0.0.1", 8788)    # 对端地址（服务端的监听地址）
ENC = "gb2312"

MY_NAME = "客户端B"  # NEW：给自己取个名字

def recv_loop(sock: socket):
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            text = data.decode(ENC, errors="ignore")
            # NEW：解析“昵称|内容”
            if "|" in text:
                sender, msg = text.split("|", 1)
            else:
                sender, msg = f"{addr[0]}:{addr[1]}", text
            print("\n[来自 {} @{}:{}] {}".format(sender, addr[0], addr[1], msg))
            print("> ", end="", flush=True)
        except OSError:
            break
        except Exception as e:
            print("\n[接收异常] {}".format(e))

def send_loop(sock: socket):
    try:
        # 可选：上线提示
        try:
            sock.sendto(f"{MY_NAME}|已上线".encode(ENC, errors="ignore"), PEER_ADDR)
        except Exception:
            pass

        while True:
            msg = input("> ")
            if msg.strip().lower() == "quit":
                print("退出聊天。")
                sock.close()
                break
            # NEW：发送时带上昵称
            payload = f"{MY_NAME}|{msg}"
            sock.sendto(payload.encode(ENC, errors="ignore"), PEER_ADDR)
    except (KeyboardInterrupt, EOFError):
        print("\n退出聊天。")
        try: sock.close()
        except: pass

def main():
    print("UDP 客户端启动，监听 {}:{}，对端 {}:{}".format(*LOCAL_BIND, *PEER_ADDR))
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(LOCAL_BIND)

    t_recv = threading.Thread(target=recv_loop, args=(s,), daemon=True)
    t_recv.start()

    send_loop(s)

if __name__ == "__main__":
    main()
