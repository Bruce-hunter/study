# -*- coding:utf-8 -*-


class Dog(object):
    def __init__(self, name='zzc', age=19):
        self.name = name
        self.age = age

    def __str__(self):
        msg = '狗的名字是%s,狗的年龄是%d' % (self.name, self.age)
        return msg

    def bark(self):
        print('---wangwangwang---')
        print(self.name)

    def run(self):
        print('---runrunrun----')
        print(self.age)


dog = Dog()
print(dog)
# dog.name = 'wangwang'
dog.bark()
