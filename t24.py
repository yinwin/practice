a = 2
b = 1
s = 0
for i in range(1, 21):
    s = a / b + s
    b, a = a, a + b
print(s)
