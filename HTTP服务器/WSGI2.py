# -*- coding:utf-8 -*-

import os
import re
import time
from Web1 import HttpHandle

documentRoot = './static'


class Application(object):
    def __init__(self, urls):
        # print('---1----')
        self.flag = 0
        self.urls = urls
        self.status = '200 OK'
        self.response_headers = [('Content-Type', 'text/html')]

    def __call__(self, env, start_response):
        # status = '200 OK'
        path = env.get('PATH_INFO', '/')
        # 判断path路径是不是带有static的静态文件路径
        para = re.match(r'(/\w*)', path).group(1)
        if path == '/':
            filename = documentRoot + '/' + 'index.html'
            f = open(filename, 'r')
            content = f.read()
            start_response(self.status, self.response_headers)
            return content
        elif para == '/static':
            file_name = re.search(r'/static/(.+)', path).group(1)
            filename = documentRoot + '/' + file_name
            # print(filename)
            try:
                f = open(filename, 'r')
            except Exception as result:
                # print(result)
                self.status = '404 not found'
                start_response(self.status, self.response_headers)
                return '====sorry ,file not found===='
            else:
                content = f.read()
                f.close()
                start_response(self.status, self.response_headers)
                return content
        else:
            for url, func in self.urls:
                if url == para:
                    self.flag = 1
                    return func(env, start_response)
            # 因为采用的是多线程，并且收到一次数据就断开连接等待下次连接的情况，所以self.flag每次的初始值都能是1
            if self.flag == 0:
                self.status = '404 not found'
                start_response(self.status, self.response_headers)
                return '====sorry ,file not found===='


def say_hello(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    msg = 'hello world'
    return msg


def show_time(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return time.ctime()


urls = [
    ('/time1', show_time),
    ('/say_hello', say_hello)
]
app = Application(urls)




