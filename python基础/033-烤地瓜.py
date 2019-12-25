# -*- coding:utf-8 -*-


class BakedSweetPotato(object):
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = '生'
        self.condiments = []

    def __str__(self):
        msg = '地瓜的生熟程度是:%s,里面放的作料有%s' % (self.cookedString, str(self.condiments))
        return msg

    def cook(self, level):
        if level != 0:
            self.cookedLevel += level
        if 0 <= self.cookedLevel <= 3:
            self.cookedString = '生'
        elif 3 <= self.cookedLevel <= 5:
            self.cookedString = '半生不熟'
        elif 5 <= self.cookedLevel <= 8:
            self.cookedString = '熟'
        else:
            self.cookedString = '烤成木炭了'

    def add_condiments(self, zuoliao):
        if zuoliao in self.condiments:
            pass
        else:
            self.condiments.append(zuoliao)



digua = BakedSweetPotato()
digua.cook(1)
digua.add_condiments('屎')
print(digua)
digua.cook(1)
digua.add_condiments('屎')
digua.add_condiments('辣椒')

print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
