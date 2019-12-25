# -*- coding:utf-8 -*-


class Dog(object):
    def __init__(self, name='zzc', age=19):
        self.name = name
        self.__age = age

    def __str__(self):
        msg = '狗的名字是%s,狗的年龄是%d' % (self.name, self.__age)
        return msg

    def __bark(self):
        print('---wangwangwang---')
        print(self.name)

    def run(self):
        print('---runrunrun----')
        self.__bark()
        print(self.__age)


dog = Dog()
print(dog)
# dog.name = 'wangwang'
dog.run()
print(dog.age)
print(dog.name)
