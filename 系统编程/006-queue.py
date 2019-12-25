# -*- coding:utf-8 -*-

import time
from multiprocessing import Queue
from multiprocessing import Process


def read(q):
    with open('../test.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
        for i in content:
            q.put(i)


def write(q):
    with open('../test1.txt', 'w', encoding='utf-8') as f:
        while True:
            if not q.empty():
                f.write(q.get())
            else:
                break


def main():
    q = Queue()
    p1 = Process(target=read, args=(q, ))
    p2 = Process(target=write, args=(q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('读写文件已经完成')


if __name__ == '__main__':
    main()

