# -*- coding:utf-8 -*-

from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.sendto('hello'.encode('utf-8'), ('20.20.20.82', 8080))
s.close()
