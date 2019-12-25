# -*- coding:utf-8 -*-

from socket import *

bind_addr = ('', 8080)
s = None


def handle():
    while True:
        print('---1----')
        newsocket, clientaddr = s.accept()
        print('---2----')
        try:
            while True:
                recv_data = newsocket.recv(1024)
                if len(recv_data) > 0:
                    print('%s:%s' % (clientaddr, recv_data))
                else:
                    print('客户端已关闭')
                    break
        finally:
            newsocket.close()
    s.close()


def main():
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(5)
    handle()


if __name__ == '__main__':
    main()
