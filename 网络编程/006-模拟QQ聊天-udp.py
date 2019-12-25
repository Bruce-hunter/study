# -*- coding:utf-8 -*-

from socket import *
from threading import Thread


def send_data(*args):
    while True:
        data = input('<<')
        args[0].sendto(data.encode('utf-8'), (args[1], args[2]))


def recv_data(*args):
    while True:
        rec_data = args[0].recvfrom(1024)
        print('\r>>%s:%s' % (rec_data[1], rec_data[0].decode('gb2312')))
        print('>>', end='')


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    bind_addr = ('', 8080)
    s.bind(bind_addr)
    ip = input('请输入你想发送的ip地址:')
    port = int(input('请输入你想发送的端口号:'))
    t1 = Thread(target=send_data, args=(s, ip, port))
    t2 = Thread(target=recv_data, args=(s, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()