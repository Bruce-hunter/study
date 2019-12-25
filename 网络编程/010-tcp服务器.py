# -*- coding:utf-8 -*-

from socket import *

bind_addr = ('', 8090)


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(bind_addr)
    s.listen(2)
    newsocket, clientaddr = s.accept()
    print('---2---')
    print(newsocket)
    print(clientaddr)
    recv_data = newsocket.recv(1024)
    print(recv_data)
    newsocket.close()
    s.close()


if __name__ == '__main__':
    main()