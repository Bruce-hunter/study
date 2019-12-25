# -*— coding:utf-8 -*-

# f = open('../test.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

f = open('../test.txt', 'a+', encoding='utf-8')
f.writelines('有一说一，确实')
f.seek(0)
print(f.readlines())
print(f.tell())
f.close()


