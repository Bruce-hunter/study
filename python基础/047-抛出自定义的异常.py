# —*- coding:utf-8 -*-


class Short(Exception):
    def __init__(self, num, num2):
        self.num = num
        self.atleast = num2


try:
    num = int(input('请输入一个你想输入的值:'))
    if num > 3:
        raise Short(num, 3)
except Short as result:
    print('你输入的数字是%d,应该输入的数字不应该大于%d'% (result.num, result.atleast))
