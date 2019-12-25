# -*- coding:utf-8 -*-
# 注意用进程池这种方法，主进程不会等待进程池中的任务全部结束后才退出，而是主进程结束了就退出，进程池中剩余的任务将不再继续执行
# 除非用到close()和join()方法或者其它方式能够使主进程堵塞

import os
from multiprocessing import Pool, Manager


def handle(q, name, old_file, new_file):
    f = open(old_file + '/' + name, 'r', encoding='utf-8')
    fw = open(new_file + '/' + name, 'w', encoding='utf-8')
    context = f.read()
    fw.write(context)
    f.close()
    fw.close()
    q.put(name)


def main():
    old_file = input('请输入你想赋值的文件夹的名字：')
    new_file = old_file + '-附件'
    # print(new_file)
    os.mkdir(new_file)
    try:
        content = os.listdir(old_file)
        # print(content)
    except Exception as result:
        print('程序遇到了错误，错误原因%s,请手动处理' % result)
    else:
        q = Manager().Queue()
        pool = Pool(5)
        for name in content:
            pool.apply_async(handle, args=(q, name, old_file, new_file))
        num = 0
        all_num = len(content)
        while True:
            q.get()
            num += 1
            copy_rate = num/all_num
            print('\r复制的进度是：%.2f%%' % (copy_rate*100), end='')
            if num == all_num:
                break
        print('')


if __name__ == '__main__':
    main()
