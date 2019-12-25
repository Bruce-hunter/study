# -*- coding:utf-8 -*-

import time
from threading import Thread


def say_sorry():
    time.sleep(5)
    print('该进程的名字是%s,id是' % Thread.name)


def say_yes():
    time.sleep(3)
    print('该进程的名字是%s,id是' % Thread.name)


def main():
    t1 = Thread(target=say_sorry)
    t2 = Thread(target=say_yes)
    t1.start()
    t2.start()
    print('线程都执行完毕了')


if __name__ == '__main__':
    main()