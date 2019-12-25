# -*- coding:utf-8 -*-

import time
from multiprocessing import Pool
from multiprocessing import Manager


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
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply_async(read, args=(q, ))
    pool.apply_async(write, args=(q, ))
    pool.close()
    pool.join()
    print('读写文件已经完成')


if __name__ == '__main__':
    main()
