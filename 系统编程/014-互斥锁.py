# -*- coding:utf-8 -*-

import time
from threading import Lock
from threading import Thread

g_num = 0


def func_a(mutex):
    print('---222---')
    global g_num
    for i in range(1000000):
        if mutex.acquire(False):
            g_num += 1
            print('--1---')
            # time.sleep(1)
            mutex.release()
        else:
            g_num += 1
        # 下面这种写法会报错，因为当一个用非堵塞方式，一个用堵塞方式时，一旦堵塞方式抢到锁，而非堵塞方式没抢到，但他不会堵塞而是继续执行
        # 等到执行到解锁步骤时会报错，因为当前锁对象并没有上锁
        # mutex.acquire(False)
        # g_num += 1
        # print('--1---')
        # # time.sleep(1)
        # mutex.release()
    print('进程a最终加的的结果是%d' % g_num)


def func_b(mutex):
    # time.sleep(5)
    print('---111')
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('进程b最终加的的结果是%d' % g_num)


def main():
    mutex = Lock()
    t1 = Thread(target=func_a, args=(mutex,))
    print('t1的名字是%s' % t1.name)
    t2 = Thread(target=func_b, args=(mutex,))
    print('t2的名字是%s' % t2.name)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # 最终结果不是2000000的原因，在执行num+=1的过程中，首先执行num+1然后得到的值赋给num变量，这是两步进行的，所以可能会出现两个线程同时执行的情况，实际上只加了一次
    print('最终结果是%d' % g_num)


if __name__ == '__main__':
    main()