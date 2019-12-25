# -*- coding:utf-8 -*-

import select
import re
from socket import *

bind_addr = ('', 7788)
epoll = select.epoll()
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(bind_addr)
s.listen(10)
epoll.register(s.fileno(), select.EPOLLIN)
connecttion = {s.fileno(): s}
flag = 0
content = {}
while True:
    epoll_list = epoll.poll()
    for fd, event in epoll_list:
        socket1 = connecttion[fd]
        if socket1 == s:
            print('接收客户端的连接')
            newsocket, clientaddr = socket1.accept()
            connecttion[newsocket.fileno()] = newsocket
            epoll.register(newsocket.fileno(), select.EPOLLIN)
        elif event == select.EPOLLIN:
            recvdata = socket1.recv(1024)
            if recvdata:
                print('收到数据')
                recvdata = recvdata.decode('utf-8')
                data_list = recvdata.splitlines()
                req = data_list[0]
                result = re.split(r' ', req)
                print(result)
                if result[0] == 'GET' and result[1] == '/':
                    print('---1---')
                    content[fd] = result[1]
                    epoll.modify(fd, select.EPOLLOUT)
            else:
                print('客户端断开连接')
                epoll.unregister(fd)
                del connecttion[fd]
                del content[fd]
                socket1.close()
        elif event == select.EPOLLOUT:
            print('---2---')
            if flag % 2 == 0 and content[fd] == '/':
                print('---3---')
                flag += 1
                socket1.send('hello welcome to home'.encode('utf-8'))
            elif flag % 2 == 0 and content[fd] != '/':
                flag += 1
                socket1.send('hello'.encode('utf-8'))
            else:
                flag += 1
                epoll.modify(fd, select.EPOLLIN)
