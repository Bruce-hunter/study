# -*- coding:utf-8 -*-

import sys
from socket import *
import struct

ip = ''
num = 0
f = None
file = None
s = None


def check(func):
    def wrapper():
        if len(sys.argv) != 3:
            print('请使用正确的格式调用\ntips: python3 xxx.py server_ip filename')
            exit()
        else:
            global file, ip
            file = sys.argv[2]
            ip = sys.argv[1]
            func()
    return wrapper


@check
def handle():
    global num, f
    cmd_buf = struct.pack("!H6sb5sb", 1, file.encode('utf-8'), 0, b'octet', 0)
    s.sendto(cmd_buf, (ip, 69))
    while True:
        recv_data, recv_addr = s.recvfrom(1024)
        # recvDataLen = len(recvData)
        cmdtuple = struct.unpack("!HH", recv_data[:4])
        if cmdtuple[0] == 3:
            if cmdtuple[1] == 1:
                f = open('./' + file, 'ab')
            if num+1 == cmdtuple[1]:
                f.write(recv_data[4:])
                num += 1
                ack_buf = struct.pack("!HH", 4, num)
                s.sendto(ack_buf, recv_addr)
            if len(recv_data) < 516:
                break
        elif cmdtuple[0] == 5:
            print('出现了错误')
            break


def main():
    global s
    s = socket(AF_INET, SOCK_DGRAM)
    handle()


if __name__ == '__main__':
    main()

