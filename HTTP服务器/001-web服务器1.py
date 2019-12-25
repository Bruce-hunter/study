# -*- coding:utf-8 -*-

import re
from socket import *

bind_addr = ('', 80)


def handle(new_socket, clientaddr):
    recv_data = new_socket.recv(4096)
    print(recv_data.decode('utf-8'))
    recv_data = recv_data.decode('utf-8')
    data_list = recv_data.splitlines()
    print(data_list)
    # req = 'GET /?a=1&b=2 HTTP/1.1'
    req = data_list[0]
    print(req)
    result = re.search(r'\b(\w+)\b', req)
    result2 = re.split(r' ', req)
    print(result2)
    if result2:
        if result2[0] == 'GET' and result2[1] == '/':
            new_socket.send('hello world welcome to home'.encode('utf-8'))
        else:
            new_socket.send('welcome'.encode('utf-8'))


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(10)
    new_socket, clientaddr = s.accept()
    handle(new_socket, clientaddr)


if __name__ == '__main__':
    main()
