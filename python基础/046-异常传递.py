# -*- coding:utf-8 -*-


import time
try:
    print('---1---')
    # f = open('test.txt')
    print('---2---')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")
