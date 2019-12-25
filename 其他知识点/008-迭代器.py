# -*- coding:utf-8 -*_


from collections.abc import Iterable
from collections.abc import Iterator


iter_a = (x for x in range(10))
print(isinstance(iter_a, Iterable))
print(isinstance(iter_a, Iterator))


def func(num):
    a, b = 0, 1
    while num < 5:
        yield b
        a, b = b, a+b
        num += 1


a = func(1)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))