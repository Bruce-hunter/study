# -*- coding:utf-8 -*-
import sys

class Person(object):
    def __new__(cls):
        print('---1---')
        return object.__new__(cls)

    def __init__(self):
        print('===1===')
        self.name = 'laowang'

    def __str__(self):
        return '---3----'
print(id(Person))
a = Person()
print(sys.getrefcount(Person))
del a
print(sys.getrefcount(a))

