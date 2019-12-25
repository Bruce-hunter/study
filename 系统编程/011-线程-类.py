# -*- coding:utf-8 -*-

import time
from threading import Thread


class ThreadTest(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)


def main():
    t = ThreadTest()
    t.start()
    t.join()
    print('主线程马上结束')


if __name__ == '__main__':
    main()
