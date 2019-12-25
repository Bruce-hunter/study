# -*— coding:utf-8 -*-

from threading import Thread

g_num = 0


def func_a():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('进程a最终加的的结果是%d' % g_num)


def func_b():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('进程b最终加的的结果是%d' % g_num)


def main():
    t1 = Thread(target=func_a)
    print('t1的名字是%s' % t1.name)
    t2 = Thread(target=func_b)
    print('t2的名字是%s' % t2.name)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # 最终结果不是2000000的原因，在执行num+=1的过程中，首先执行num+1然后得到的值赋给num变量，这是两步进行的，所以可能会出现两个线程同时执行的情况，实际上只加了一次
    print('最终结果是%d' % g_num)


if __name__ == '__main__':
    main()
