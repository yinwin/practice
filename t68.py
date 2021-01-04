t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(5):
    a = t[14]
    for j in range(14, -1, -1):
        t[j] = t[j - 1]
    t[0] = a

print(t)