# -*— coding:utf-8 -*_


#用递归函数计算5的阶乘

def get_num(num):
    if num == 1:
        return 1
    else:
        num = num * get_num(num-1)
    return num


print(get_num(1))

