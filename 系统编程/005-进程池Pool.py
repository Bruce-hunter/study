# -*- coding:utf-8 -*-

import os, random, time
from multiprocessing import Pool


def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


p = Pool(3)

for i in range(5):
    p.apply_async(worker, (i, ))

time.sleep(5)
print("----start----")
p.close() #关闭进程池，关闭后po不再接收新的请求
p.join() #等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")
