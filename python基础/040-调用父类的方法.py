# -*- coding:utf-8 -*_


class Animals(object):
    def __init__(self):
        self.zhonglei = 'Dog'

    def run(self):
        print('%s正在跑' % self.name)

    def bark(self):
        print('%s正在叫' % self.name)


class Dog(Animals):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__()

    def fly(self):
        print('%s正在飞行' % self.name)

    def run(self):
        print('%s就他妈不跑' % self.name)
        super().run()


a = Dog('xiaotianquan', 18)
a.run()