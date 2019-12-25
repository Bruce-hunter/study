# -*- coding:utf-8 -*-
import types


class Person(object):
    status = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('----人正在跑')

    def sing(self):
        print('----人正在唱歌')


@classmethod
# talk = classmethod(talk)
def talk(cls):
    print(cls)
    print('---人正在说话')
    print(cls.status)


def walk(self):
    print('-----%s正在走路' % self.name)


def say():
    print('---正在说你好')


p = Person('zhangfei', 18)

# p.sex = 'female'
# print(p.sex)
#
# # p.walk = walk
# # p.walk()
# p.run()
# Person.talk = talk
# Person.talk()
print(p)
p.walk = types.MethodType(walk, p)
print(types.MethodType(walk, p))
print(p.walk)
print(walk)
p.walk()
a = walk
b = walk
print(id(a))
print(id(p.walk))
print(id(b))
print(id(walk))

# Person.say = say
# Person.say()

# Person.walk = walk
# p = Person('zhangfei', 18)
# p.walk()