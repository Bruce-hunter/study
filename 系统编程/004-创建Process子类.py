# -*- coding:utf-8 -*-

import time
from multiprocessing import Process


class TestProcess(Process):
    def run(self):
        start_time = time.time()
        print(start_time)
        print('---子进程已经开始执行-----')
        time.sleep(3)
        end_time = time.time()
        print(end_time)
        print('子进程%s的执行时间为%d秒' % (self.name, end_time - start_time))


def main():
    t = TestProcess()
    t.start()
    t.join()
    print('子进程执行完毕')


if __name__ == '__main__':
    main()