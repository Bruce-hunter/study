try:
    f = open('test.txt', 'r')
except Exception as result:
    print(result)
else:
    content = f.read()
    print(content)
finally:
    print('---1---')
    print(f)
    f.close()
    print('---2---')
<<<<<<< HEAD
    print('---3---')
    print('---4---')
=======
    print('---7---')
>>>>>>> dev
