# -*- coding:utf-8 -*-

import re
from socket import *
from threading import Thread

documentRoot = './html'
bind_addr = ('', 7788)


def handle(newsocket, clientaddr):
    # while True:
    print('---1---')
    recv_data = newsocket.recv(4096)
    print('---2---')
    print(recv_data)
    if recv_data:
        recv_data = recv_data.decode('utf-8').splitlines()
        result = re.split(r' ', recv_data[0])
        if result[1] == '/':
            print('---3---')
            file_name = documentRoot + '/' + 'index.html'
            print(file_name)
        else:
            print('---4---')
            filename = re.search(r'^/(.+\b)', result[1])
            file_name = documentRoot + '/' + filename.group(1)
            print(file_name)
        try:
            f = open(file_name, 'r')
        except Exception as result:
            print(result)
            responseheaderlines = "HTTP/1.1 404 not found\r\n"
            responseheaderlines += "\r\n"
            responsebody = "====sorry ,file not found===="
            print('---5---')
        else:
            responseheaderlines = "HTTP/1.1 200 OK\r\n"
            responseheaderlines += "\r\n"
            responsebody = f.read()
            f.close()
        finally:
            print('---6---')
            responsebody = responseheaderlines + responsebody
            newsocket.send(responsebody.encode('utf-8'))
            print('---7---')
            newsocket.close()
            # break


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(10)
    try:
        while True:
            newsocket, clientaddr = s.accept()
            t1 = Thread(target=handle, args=(newsocket, clientaddr))
            t1.start()
    finally:
        s.close()


if __name__ == '__main__':
    main()
