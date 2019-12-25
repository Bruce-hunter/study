# -*- coding:utf-8 -*-


# 生成一个[[1,2,3],[4,5,6]....]的列表最大值在100以内
a = [[x, y, z] for x in range(1, 98, 3) for y in range(2, 99, 3) for z in range(3, 100, 3) if y - x == 1 and z - y == 1]
print(a)

# for x in range(1, 98, 3):
#     for y in range(2, 99, 3):
#         for z in range(3, 100, 3):
#             if y - x == 1 and z - y == 1:
#                 print([x, y, z])
