# -*- coding:utf-8 -*-

import os
import time


ret = os.fork()
if ret == 0:
    time.sleep(4)
    print('hahah')
    print('子进程的id是%d,它的父进程id是%d' % (os.getpid(), os.getppid()))
else:
    print('xixiix')
    print('父进程的id是%d' % os.getpid())
