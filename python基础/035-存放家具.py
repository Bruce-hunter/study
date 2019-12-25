# -*-coding:utf-8 -*-


class Home(object):
    def __init__(self, area):
        self.area = area
        self.goods = []

    def __str__(self):
        msg = '家的剩余面积是%d，床的名字是%s' % (self.area, str(self.goods[-1]))
        return msg

    def add_bed(self, bed):
        if bed.area <= self.area:
            self.area = self.area - bed.area
            self.goods.append(bed.name)
        else:
            print('屋子太小，床太大，放不下辣')


class Bed(object):
    def __init__(self, area, name):
        self.area = area
        self.name = name

    def __str__(self):
        pass


bed = Bed(18, '席梦思')
home = Home(88)
home.add_bed(bed)
print(home)