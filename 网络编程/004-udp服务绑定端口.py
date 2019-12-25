# -*- coding:utf-8 -*-

from socket import *


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    bind_addr = ('', 8080)
    s.bind(bind_addr)
    content = s.recvfrom(1024)
    print(content)


if __name__ == '__main__':
    main()
