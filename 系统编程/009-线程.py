# coding=utf-8

# import time
#
#
# def say_sorry():
#     print("亲爱的，我错了，我能吃饭了吗？")
#     time.sleep(1)
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         say_sorry()


import threading
import time


def say_sorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=say_sorry)
        t.start() #启动线程，即让线程开始执行
