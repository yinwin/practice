i = 0
l = []
k=0
m=0
for j in range(40):
    j +=1 
    l.append(j)
i = 0
while m < 39:
    if l[i] != 0:
        k += 1
    if k == 3:
        l[i] = 0
        k = 0
        m += 1
    i += 1
    if i == 40:
        i = 0

print(l)
'''
for n in range(40):
    while [n] != 0:
        print(n)
'''
