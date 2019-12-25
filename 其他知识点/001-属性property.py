# -*- coding:utf-8 -*-
# class Test(object):
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#
# t = Test()
# print(t.get_age())
# t.set_age(22)
# print(t.get_age())


# class Test(object):
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#     def del_age(self):
#         del self.__age
#
#     age = property(get_age, set_age, del_age, doc='wwww')
#
#
# t = Test()
# print(t.age)
# t.age = 100
# print('---1---')
# print(Test.age.__doc__)
# print('---2---')
#
# del t.age
# print(dir(t))
# print(t.age)

class Test(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


t = Test()
print(t.age)
t.age = 100
print(t.age)