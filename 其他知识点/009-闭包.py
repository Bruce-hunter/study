# -*- coding:utf-8 -*_


# nonlocal
num = 10


def func_out():
    num = 100
    def func():
        def func_in():
            nonlocal num
            num = 10
            print(num)
        func_in()
        print(num)
    func()
    print(num)


func_out()


# 闭包
def func_b(num):

    def func_in_b():
        print(num)
    return func_in_b


a = func_b(5)
a()




