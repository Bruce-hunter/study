# -*- coding:utf-8 -*-

from socket import *
from threading import Thread

s = None
bind_addr = ''
ip = ''
port = 0


def send_data():
    while True:
        data = input('<<')
        s.sendto(data.encode('utf-8'), (ip, port))


def recv_data():
    while True:
        rec_data = s.recvfrom(1024)
        print('\r>>%s:%s' % (rec_data[1], rec_data[0].decode('gb2312')))
        print('>>', end='')


def main():
    global s, bind_addr, ip, port
    s = socket(AF_INET, SOCK_DGRAM)
    bind_addr = ('', 8090)
    s.bind(bind_addr)
    ip = input('请输入你想发送的ip地址:')
    port = int(input('请输入你想发送的端口号:'))
    t1 = Thread(target=send_data)
    t2 = Thread(target=recv_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()