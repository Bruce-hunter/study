def main():
    try:
        print('---1---')
        return 1
    finally:
        print('---2---')


if __name__ == '__main__':
    a = main()
    print(a)