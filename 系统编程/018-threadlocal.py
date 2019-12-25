# -*- coding:utf-8 -*-

from threading import Thread, local, current_thread

student = local()


def process_student():
    std = student.name
    print('Hello, %s (in %s)' % (std, current_thread().name))


def func_a(name):
    student.name = name
    process_student()


def main():
    t1 = Thread(target=func_a, args=('dongGe',), name='Thread-A')
    t2 = Thread(target=func_a, args=('老王',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()