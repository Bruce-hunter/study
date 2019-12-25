import sys
import time
import gevent

from gevent import socket, monkey
monkey.patch_all()


def handle_request(conn):
    while True:
        print('---3---')
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("recv:", data)
        conn.send(data)


def server(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(5)
    while True:
        print('--1--')
        cli, addr = s.accept()
        print('---2---')
        # gevent.spawn(handle_request, cli)
        handle_request(cli)
        print('---4---')


if __name__ == '__main__':
    server(7788)