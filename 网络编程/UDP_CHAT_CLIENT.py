# -*- coding: gb2312 -*-
import threading
from socket import *

# === ���� ===
LOCAL_BIND = ("0.0.0.0", 8089)      # ���������˿ڣ������˴���
PEER_ADDR  = ("127.0.0.1", 8788)    # �Զ˵�ַ������˵ļ�����ַ��
ENC = "gb2312"

MY_NAME = "�ͻ���B"  # NEW�����Լ�ȡ������

def recv_loop(sock: socket):
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            text = data.decode(ENC, errors="ignore")
            # NEW���������ǳ�|���ݡ�
            if "|" in text:
                sender, msg = text.split("|", 1)
            else:
                sender, msg = f"{addr[0]}:{addr[1]}", text
            print("\n[���� {} @{}:{}] {}".format(sender, addr[0], addr[1], msg))
            print("> ", end="", flush=True)
        except OSError:
            break
        except Exception as e:
            print("\n[�����쳣] {}".format(e))

def send_loop(sock: socket):
    try:
        # ��ѡ��������ʾ
        try:
            sock.sendto(f"{MY_NAME}|������".encode(ENC, errors="ignore"), PEER_ADDR)
        except Exception:
            pass

        while True:
            msg = input("> ")
            if msg.strip().lower() == "quit":
                print("�˳����졣")
                sock.close()
                break
            # NEW������ʱ�����ǳ�
            payload = f"{MY_NAME}|{msg}"
            sock.sendto(payload.encode(ENC, errors="ignore"), PEER_ADDR)
    except (KeyboardInterrupt, EOFError):
        print("\n�˳����졣")
        try: sock.close()
        except: pass

def main():
    print("UDP �ͻ������������� {}:{}���Զ� {}:{}".format(*LOCAL_BIND, *PEER_ADDR))
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(LOCAL_BIND)

    t_recv = threading.Thread(target=recv_loop, args=(s,), daemon=True)
    t_recv.start()

    send_loop(s)

if __name__ == "__main__":
    main()
