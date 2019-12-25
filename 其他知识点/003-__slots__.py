# -*- coding:utf-8 -*-


class Dog(object):
    status = 1
    __slots__ = ('name', )

    def __init__(self, name):
        self.name = name
        # self.age = 19

    def run(self):
        print('大狗在跑步')


class WangCai(Dog):
    def __init__(self):
        self.name = 'wangcai'


d = Dog('w')
Dog.status = 2
d.run()
print(Dog.status)


w = WangCai()
w.age = 18
print(w.age)

