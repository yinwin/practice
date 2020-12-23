def reduceNum(n):
    print('{} ='.format(n))
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字！')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        # print('a')
        for index in range(2, n+1):
            # print('b')
            if n % index == 0:
                n = n // index
                print(index)
                # if n == 1:
                #   print(index)
                # else:
                #    print('{}'.format(index))
                break
reduceNum(90)
