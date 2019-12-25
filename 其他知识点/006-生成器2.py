# -*- coding:utf-8 -*-


def func():
    n = 0
    a, b = 0, 1
    while n < 10:
        result = yield b
        print(result)
        a, b = b, a+b
        n += 1


a = func()
print(a.send(None))
print(a.__next__())