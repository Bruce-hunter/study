# -*- coding:utf-8 -*-

import select
import sys
from socket import *


server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server.bind(('', 7788))
server.listen(5)
inputs = [server]

running = True

while True:

    # 调用 select 函数，阻塞等待
    print('---2---')
    readable, writeable, exceptional = select.select(inputs, [], [])
    print(readable)
    print(len(readable))
    print('---1---')
    # 数据抵达，循环
    for sock in readable:
        print('--3---')
        # 监听到有新的连接
        if sock == server:
            conn, addr = server.accept()
            # select 监听的socket
            inputs.append(conn)
            print(inputs)

        # 监听到键盘有输入
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break

        # 有数据到达
        else:
            # 读取客户端连接发送的数据
            data = sock.recv(1024)
            if data:
                print(sock)
                print(data)
                sock.send(data)
            else:
                # 移除select监听的socket
                inputs.remove(sock)
                sock.close()

    # 如果检测到用户输入敲击键盘，那么就退出
    if not running:
        break

server.close()