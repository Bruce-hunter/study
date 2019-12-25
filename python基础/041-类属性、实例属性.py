# -*- coding:utf-8 -*-


class Country(object):
    country = 'China'

    def __init__(self):
        self.country = 'America'


c = Country()
print(c.country)
print(Country.country)