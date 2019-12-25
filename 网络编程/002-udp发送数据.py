# -*- coding:utf-8 -*-

from socket import *


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    send_addr = ('20.20.20.82', 8080)
    send_data = input('请输入你想发送的数据:')
    s.sendto(send_data.encode('utf-8'), send_addr)
    s.close()


if __name__ == '__main__':
    main()
