# -*- coding:utf-8 -*-


class Dog(object):
    def __init__(self, name='zzc', age=19):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('调用了new方法根据传进来的类创建了一个对象')
        return object.__new__(cls)

    def __str__(self):
        msg = '狗的名字是%s,狗的年龄是%d' % (self.name, self.age)
        return msg

    def bark(self):
        print('---wangwangwang---')
        print(self.name)

    def run(self):
        print('---runrunrun----')
        print(self.age)

    def change_attr(self, name, age):
        self.name = name
        self.age = age



dog = Dog()
print(dog)
# dog.name = 'wangwang'
dog.bark()
