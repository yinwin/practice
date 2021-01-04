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

sump = 1
while True:
    for j in range(5):
        if (sump - 1) % 5 == 0 and sump - 1 != 0:
            sump = 4 * (sump - 1) / 5
        print(sump)
    else: sump  = sump + 1
       
    if sump > 1000:
        break
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