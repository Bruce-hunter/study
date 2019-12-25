# -*- coding:utf-8 -*-


set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# 交集
set_c = set_a & set_b

# 并集
set_d = set_a | set_b

# 差集（set_a中存在，set_b中不存在的）
set_e = set_a - set_b

# 对称差集（(在set_a或set_b中，但不会同时出现在二者中)）
set_f = set_a ^ set_b

print(set_c)
print(set_d)
print(set_e)
print(set_f)