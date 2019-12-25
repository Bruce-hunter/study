# -*- coding:utf-8 -*-

from socket import *
from threading import Thread

s = None
bind_addr = ('', 8080)


def handle(newsocket, clientaddr):
    while True:
        recv_data = newsocket.recv(1024)
        if recv_data:
            print('%s:%s' % (clientaddr, recv_data))
        else:
            print('%s客户端发送断开连接请求' % str(clientaddr))
            break
    newsocket.close()
    # s.close()


def main():
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(10)
    try:
        while True:
            print('---1---')
            newsocket, clientaddr = s.accept()
            print('---2---')
            t = Thread(target=handle, args=(newsocket, clientaddr))
            t.start()
            # newsocket.close()
    finally:
        s.close()


if __name__ == '__main__':
    main()
