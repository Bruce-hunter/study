# -*- coding:utf-8 -*-


def select_s(pre=1):

    def student_a(func):
        def wrapped(name):
            print('%s是一个好学生' % name)
            func(name)
        return wrapped

    def student_b(func):
        def wrapped(name):
            print('%s是一个坏学生' % name)
            func(name)
        return wrapped
    if pre == 0:
        return student_a
    else:
        return student_b


@select_s(0)
def print_a(name):
    print('所以%s是爹' % name)


@select_s(1)
def print_b(name):
    print('所以%s是儿子' % name)


print_a('zhangfei')
print_b('zhangyang')


