# -*- coding:utf-8 -*-


class Dog(object):
    def __init__(self, name='zzc', age=19):
        self.name = name
        self.age = age

    def bark(self):
        print('---wangwangwang---')
        print(self.name)

    def run(self):
        print('---runrunrun----')
        print(self.age)


dog = Dog()
# dog.name = 'wangwang'
dog.bark()