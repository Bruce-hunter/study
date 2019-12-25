# -*- coding:utf-8 -*-


class YuanLei(type):
    def __new__(cls, class_name, class_parents, class_attr):
        newAttr = {}
        for key, value in class_attr.items():
            if not key.startswith('__'):
                newAttr[key.upper()] = value
        # return super().__new__(class_name, class_parents, newAttr)
        # return type(class_name, class_parents, newAttr)
        # return super().__new__(cls, class_name, class_parents, newAttr)
        return type.__new__(cls, class_name, class_parents, newAttr)


class Person(object, metaclass=YuanLei):
    bar = 'bar'

    def __init__(self):
        self.name = 'zzc'

    def run(self):
        print('run')


p = Person()
print(p.BAR)
# print(p.NAME)
# p.run()
