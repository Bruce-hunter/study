# -*- coding:utf-8 -*-

import sys
import re
from socket import *
from multiprocessing import Process

# documentRoot = './html'
pythonRoot = './wsgiPy'


class HttpHandle(object):
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.newsocket = None
        self.headers_set = None
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
        # print('---2---')
        # print(recv_data)
        if recv_data:
            recv_data = recv_data.decode('utf-8').splitlines()
            result = re.split(r' ', recv_data[0])
            env = {'REQUEST_METHOD': 'GET', }
            if result[1].endswith('py'):
                filename = re.search(r'^/(.+\b)', result[1]).group(1)
                modulename = filename.split('.')[0]
                # print('---3---')
            try:
                m = __import__(modulename)
            except Exception as result:
                # print(result)
                responseheaderlines = "HTTP/1.1 404 not found\r\n"
                responseheaderlines += "\r\n"
                responsebody = "====sorry ,file not found===="
                # print('---5---')
            else:
                responsebody = m.application(env, self.start_response)
                responsebody = str(responsebody)
                # print(responsebody)
                status, response_headers = self.headers_set
                # print(response_headers)
                responseheaderlines = "HTTP/1.1 %s\r\n" % status
                # print(responseheaderlines)
                for header in response_headers:
                    header = '%s: %s' % header
                    header += "\r\n"
                    # print(header)
                    responseheaderlines = responseheaderlines + header
                # print('---7---')
                responseheaderlines += "\r\n"
                # print(responseheaderlines)
            finally:
                # print('---6---')
                responsebody = responseheaderlines + responsebody
                self.newsocket.send(responsebody.encode('utf-8'))
                # print('---7---')
                self.newsocket.close()

    def start_response(self, status, response_headers):
        serverheaders = [
            ('Date', 'Tue, 31 Mar 2016 10:11:12 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + serverheaders]


if __name__ == '__main__':
    sys.path.insert(1, pythonRoot)
    http = HttpHandle()
    http.bind(7788)
    http.listen(10)
    http.start()