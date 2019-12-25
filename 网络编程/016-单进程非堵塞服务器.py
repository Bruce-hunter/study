# -*— coding:utf-8 -*-

from socket import *

server_list = []


def main():
    bind_addr = ('', 8080)
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(bind_addr)
    s.listen(1000)
    s.setblocking(False)
    while True:
        # print('---1---')
        try:
            newsocket, clientaddr = s.accept()
        except Exception as result:
            pass
        else:
            newsocket.setblocking(False)
            server_list.append((newsocket, clientaddr))
        for newsocket, clientaddr in server_list:
            try:
                recv_data = newsocket.recv(1024)
                if recv_data:
                    print('%s:%s' % (str(clientaddr), recv_data))
                else:
                    print('%s客户端已关闭' % str(clientaddr))
                    newsocket.close()
                    server_list.remove((newsocket, clientaddr))
            except Exception as result:
                pass


if __name__ == '__main__':
    main()
