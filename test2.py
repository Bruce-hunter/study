# -*- coding:utf-8 -*-


# class Dog(object):
#     def run(self):
#         print('狗正在泡')
#
#
# class XiaoTian(Dog):
#     def run_a(self):
#         print('gouzhengziarun')
#
#
# class XiaoTianSon(XiaoTian):
#     def run_b(self):
#         print('gouzi')
#         # Dog.run(self)
#         super(XiaoTianSon, self).run_a()
#
#
# print(XiaoTianSon.__mro__)
# x = XiaoTianSon()
# x.run_b()
class Person(object):
    def __new__(cls):
        print('---1---')
        return object.__new__(cls)

    def __init__(self):
        print('===1===')
        self.name = 'laowang'

    def __str__(self):
        return '---3----'


class Ren(Person):
    def __new__(cls):
        print(id(cls))
        print('---2---')
        return super().__new__(cls)

    def __init__(self):
        print(id(self))
        print('===2====')
        # super().__init__()
        Person.__init__(self)

    def __str__(self):
        return '---4---' + super().__str__()

print(id(Ren))
r = Ren()
print(id(r))
print(r)
print(r.name)
p = Person()
print(p.name)
