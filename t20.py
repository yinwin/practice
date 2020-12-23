a = 100
L = 100
for i in range(2, 11):
    a = 100/(2 ** (i-1))
    L = L + 2*a
print(L, a/2)
