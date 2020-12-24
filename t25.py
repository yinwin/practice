
s = 0
for i in range(1, 21):
    a=1
    for j in range(1, i+1):
        a = a * j
    s = s + a
print(s)
