# -*- coding:utf-8 -*-

from socket import *


def main():
    # 服务未绑定端口，不知道该向哪发
    s = socket(AF_INET, SOCK_DGRAM)
    # recv_addr = ('20.20.20.82', 8080)
    content = s.recvfrom(1024)
    print(content)


if __name__ == '__main__':
    main()
