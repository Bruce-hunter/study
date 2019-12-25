# -*- coding:utf-8 -*-
# a = [1, 2, 2]
# b = 1
#
#
# def test():
#     # a = [1, 1]
#     # global a
#     # a = [1, 2, 3]
#     # global a
#     b = 2
#     global b
#     b = 3
#     print(b)
#
#
# def test2():
#     print(b)
#
#
# test()
# test2()
# def test(*a):
#     print(a)
# a = [1,2,3]
# test(*a)
import time
# a = 1
#
#
# def test(num: int) -> int:
#     num += num
#     return num
#
#
# test(a)
# # print(a)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = 3
# if c in a:
#     print(c)

#
# class Info(object):
#     num = 0
#     print('zzc')
#
#     def __init__(self):
#         pass
#
#
# def test():
#     num = 0
#     print('zzr')


# def zhuang(func):
#     def print_num():
#         func()
#         print('你必须先装个逼')
#     return print_num
#
#
# @zhuang
# # test1 = zhuang(test1)
# def test1():
#     print('怎么才能引起别人的注意？')
#
#
# test1()


class Dog(object):
    def __new__(cls, name):
        print('---1---')
        print(name)
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print(self.name)
        super().__init__()



# class WangCai(Dog):
#     def __new__(cls, name):
#         super().__new__(cls, name)

w = Dog('zhangfei')
w.name = 'laowang'
print(w.name)

# print(w.name)
# print(w.age)
