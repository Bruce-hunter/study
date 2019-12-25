# -*- coding:utf-8 -*-


class Dog(object):
    def bark(self):
        print('---wangwangwang---')
        # print(self.name)

    def run(self):
        print('---runrunrun----')
        # print(self.age)


dog = Dog()
dog.name = 'wangwang'
dog.bark()