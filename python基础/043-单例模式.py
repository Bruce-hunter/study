# -*- coding:utf-8 -*-


class People(object):
    Isnot = 0
    isuse = 0

    def __init__(self):
        if People.isuse == 0:
            super().__init__()
            People.isuse = 1
        else:
            pass

    def __new__(cls, *args, **kwargs):
        if not cls.Isnot:
            cls.Isnot = 1
            cls.new_ob = super().__new__(cls)
            #调用出错
            return cls.new_ob
        else:
            return cls.new_ob

p = People()
print(id(p))
print('---111')
p2 = People()
print(id(p2))