# -*- coding:utf-8 -*-

from socket import *

server_info = ('20.20.20.82', 8080)


def main():
    s = socket()
    s.connect(server_info)
    s.send('hello'.encode('utf-8'))


if __name__ == '__main__':
    main()
