# -*— coding:utf-8 -*-

import time


def func_a():
    while True:
        print('---a-1---')
        yield
        print('---a-2---')


def func_b():
    while True:
        print('---b-1---')
        yield
        print('---b-2---')


def main():
    a = func_a()
    b = func_b()
    while True:
        a.__next__()
        b.__next__()


if __name__ == '__main__':
    main()
