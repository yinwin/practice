a = input('输入四个数字:\n')
b = []
for i in a:
    b.append((int(i) + 5) % 10)
for j in range(2):
    b[j], b[3-j] = b[3-j], b[j]
for n in b:
    print(n,end='')


