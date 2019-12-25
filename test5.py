# -*- coding:utf-8 -*-

# epoll仅能支持linux(Only supported on Linux 2.5.44 and newer)

import time
import select
from socket import *

flag = 0
s = None
epoll = None
bind_addr = ('', 7788)
connection = {}


def handle():
    global s, connection, epoll, flag
    while True:
        events = epoll.poll()
        for fd, event in events:
            server_socket = connection[fd]
            if server_socket == s:
                new_socket, client_addr = server_socket.accept()
                connection[new_socket.fileno()] = new_socket
                epoll.register(new_socket.fileno(), select.EPOLLIN)
            elif event == select.EPOLLIN:
                print('需要接收数据')
                recv_data = server_socket.recv(1024)
                if recv_data:
                    print(recv_data)
                    epoll.modify(fd, select.EPOLLOUT)
                else:
                    print('客户端关闭')
                    epoll.unregister(fd)
                    del connection[fd]
                    server_socket.close()
            elif event == select.EPOLLOUT:
                if flag % 2 == 0:
                    flag += 1
                    server_socket.send('ok'.encode('utf-8'))
                else:
                    flag += 1
                    epoll.modify(fd, select.EPOLLIN)


def main():
    global bind_addr, s, epoll, connection
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(10)
    epoll = select.epoll()
    epoll.register(s.fileno(), select.EPOLLIN)
    connection[s.fileno()] = s
    handle()


if __name__ == '__main__':
    main()
