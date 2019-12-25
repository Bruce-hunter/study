# -*- coding:utf-8 -*-

import sys
import re
from socket import *
from multiprocessing import Process

documentRoot = './static'
pythonRoot = './wsgiPy'


class HttpHandle(object):
    def __init__(self, app=None):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.new_socket = None
        self.headers_set = None
        self.app = app
        # self.ip = ip
        # self.port = port

    def bind(self, port, ip=''):
        self.socket.bind((ip, port))

    def listen(self, num):
        self.socket.listen(num)

    def start(self):
        while True:
            self.new_socket, client_addr = self.socket.accept()
            # print('---2---')
            t1 = Process(target=self.handle)
            # print('---3---')
            t1.start()
            # print('---4---')
            self.new_socket.close()

    def handle(self):
        recv_data = self.new_socket.recv(4096)
        # print('---2---')
        # print(recv_data)
        if recv_data:
            recv_data1 = recv_data.decode('utf-8').splitlines()
            # print(recv_data)
            result = re.split(r' ', recv_data1[0])
            # path = re.search(r'/static/(.*)', result[1])
            env = dict()
            env['wsgi.version'] = (1, 0)
            env['wsgi.input'] = recv_data
            env['REQUEST_METHOD'] = result[0]  # GET
            env['PATH_INFO'] = result[1]  # /index.html
            response_body = self.app(env, self.start_response)
            status, response_headers = self.headers_set
            responseheaderlines = "HTTP/1.1 %s\r\n" % status
            for header in response_headers:
                header = '%s: %s' % header
                header += "\r\n"
                # print(header)
                responseheaderlines = responseheaderlines + header
            responseheaderlines += "\r\n"
            response_body = responseheaderlines + response_body
            # print(response_body)
            self.new_socket.send(response_body.encode('utf-8'))
            # print('---7---')
            self.new_socket.close()
        else:
            pass

    def start_response(self, status, response_headers):
        serverheaders = [
            ('Date', 'Tue, 31 Mar 2016 10:11:12 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + serverheaders]


def main():
    http = HttpHandle()
    http.bind(7788)
    http.listen(10)
    http.start()


if __name__ == '__main__':
    main()
