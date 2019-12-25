# -*- coding:utf-8 -*-

import greenlet

g1 = None
g2 = None


def func_a():
    global g2
    while True:
        print('---a---')
        g2.switch()


def func_b():
    global g1
    while True:
        print('---b---')
        g1.switch()


def main():
    global g1, g2
    g1 = greenlet.greenlet(func_a)
    g2 = greenlet.greenlet(func_b)
    g1.switch()


if __name__ == '__main__':
    main()
