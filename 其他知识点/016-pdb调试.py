#coding=utf-8
import pdb


def add_nums(a1, a2, a3):
    result = a1+a2+a3
    return result


def getnums_avarage(s1, s2):
    s3 = s1 + s2 + s1
    result = 0
    result = add_nums(s1, s2, s3)/3


if __name__ == '__main__':
    a = 11
    # pdb.set_trace()
    b = 12
    final = getnums_avarage(a, b)
    print(final)
