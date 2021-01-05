'''
sump = 0
for i in range(2,1000):
    if (i - 1) % 5 == 0:
        sump = i
        i = sump
        for j in range(5):
            if (sump - 1) % 5 == 0 and sump - 1 != 0:
                sump = 4 * (sump - 1) / 5
        print(i)
'''
j = 1
i = 1
sump = 2
while j < 5:
    sump = i + 1
    for j in range(5):
        i += 1
        if (sump - 1) % 5 != 0:
            break
        #print(sump)
        else: 
            j += 1
            sump = ((sump - 1)/5) * 4
for i in range(5):

    print('第%d只猴子到的时候桃子有%d,它带走了%d' % (5-i, (sump//4)*5+1,sump//4))
    sump = (sump//4) * 5 + 1
'''
if __name__ =='__main__':
    i = 0
    j = 1
    x = 0
    while(i < 5):
        x = 4 * j
        for i in range(5):
            if x % 4 != 0:
                break
            else:
                i += 1
            x = (x // 4) * 5 + 1
        j += 1
    print(x)
    '''