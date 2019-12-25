# -*- coding:utf-8 -*-

import re
from socket import *
from multiprocessing import Process

documentRoot = './html'


class HttpHandle(object):
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # self.ip = ip
        # self.port = port

    def bind(self, port, ip=''):
        self.socket.bind((ip, port))

    def listen(self, num):
        self.socket.listen(num)

    def start(self):
        while True:
            self.newsocket, clientaddr = self.socket.accept()
            t1 = Process(target=self.handle, args=(clientaddr, ))
            t1.start()
            self.newsocket.close()

    def handle(self, clientaddr):
        recv_data = self.newsocket.recv(4096)
        print('---2---')
        # print(recv_data)
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
                self.newsocket.send(responsebody.encode('utf-8'))
                print('---7---')
                self.newsocket.close()


http = HttpHandle()
http.bind(7788)
http.listen(10)
http.start()