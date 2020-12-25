l = []
for i in range(10):
    s = input('input ten numbers:\n')
    l.append(int(s))
print(list(l))

for i in range(10):
    # min = i
    for j in range(9-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j] 
print(list(l))
