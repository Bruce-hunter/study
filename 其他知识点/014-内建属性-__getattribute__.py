# -*- coding:utf-8 -*-


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        if item == 'name':
            print('输入了正确的信息')
            print('--1---')
            return object.__getattribute__(self, item)
        elif item == 'age':
            print('输入了错误的信息')
            return object.__getattribute__(self, item)
        elif item == 'show':
            print('让你show')
            return object.__getattribute__(self, item)
        else:
            print('你无权访问')
            print('---1---')

    def show(self):
        return self.name


p = Person('zhangfei', 18)
p.name()
print(p.show())