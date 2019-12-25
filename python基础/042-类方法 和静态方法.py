# -*- coding:utf-8 -*-


class Dog(object):
    dog = 'xiaotianquan'

    @classmethod
    def change_name(cls, name):
        cls.dog = name

    @staticmethod
    def print_info():
        print('hahaha')


d = Dog()
d.change_name('hulaibu')
print(Dog.dog)
d.print_info()
