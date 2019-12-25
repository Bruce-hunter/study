# -*- coding:utf-8 -*-


class Test(object):
    def __init__(self, switch=True):
        self.switch = switch

    def cal(self):
        num1 = int(input('请输入你想输入的第一个值：'))
        num2 = int(input('请输入你想输入的第二个值：'))
        try:
            num1/num2
        except Exception as result:
            if self.switch:
                print(result)
            elif not self.switch:
                raise


t1 = Test(True)
t1.cal()
print('---1---')
t1 = Test(False)
t1.cal()
print('---2---')