# -*- coding:utf-8 -*-


def func_a():
    while True:
        print('---你是真的牛批---')
        yield
        print('你吼辣么大声干什么吗')


def func_b():
    while True:
        print('奥利给')
        yield
        print('遇到困难')


a = func_a()
b = func_b()

n = 0
while n <= 10:
    a.__next__()
    b.__next__()
    n += 1