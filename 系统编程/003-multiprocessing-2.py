# -*- coding:utf-8 -*-

import time
from multiprocessing import Process
import os


def func_a():
    time.sleep(5)
    print('a进程已经开始执行了')
    print('a进程的进程号是%d，他的父进程的进程号是%d' % (os.getpid(), os.getppid()))


def func_b():
    print('b进程已经开始执行了')
    print('b进程的进程号是%d，他的父进程的进程号是%d' % (os.getpid(), os.getppid()))


def main():
    p1 = Process(target=func_a, name='p1')
    p2 = Process(target=func_b, name='p2')
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
    # p1.terminate()
    print('p1进程的名字是%s' % p1.name)
    print('p2进程的名字是%s' % p2.name)
    print('p1进程的id是%d' % p1.pid)
    print('p2进程的id是%d' % p2.pid)


if __name__ == '__main__':
    main()
