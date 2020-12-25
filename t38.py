a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(float(input('input mun:\n')))
for i in range(3):
    sum = sum +a[i][i]
print(a)
print(sum)