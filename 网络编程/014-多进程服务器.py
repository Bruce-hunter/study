# -*- coding:utf-8 -*-

from socket import *
from multiprocessing import Process

s = None
bind_addr = ('', 8080)


def handle(newsocket, clientaddr):
    while True:
        recv_data = newsocket.recv(1024)
        if recv_data:
            print('%s:%s' % (clientaddr, recv_data))
        else:
            print('%s客户端发送断开连接请求' % clientaddr)
            newsocket.close()
            break
    s.close()


def main():
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(10)
    while True:
        print('---1---')
        newsocket, clientaddr = s.accept()
        print('---2---')
        p = Process(target=handle, args=(newsocket, clientaddr))
        p.start()
        newsocket.close()


if __name__ == '__main__':
    main()
