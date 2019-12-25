# -*- coding:utf-8 -*-

import time
from multiprocessing import Process

args = (1, 2, 3)


def func():
    time.sleep(5)
    for i in args:
        print(i)


p = Process()
p.start()
# p.join()
time.sleep(0.1)

print('5555')