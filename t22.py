A = ['a', 'b', 'c']
B = ['x', 'y', 'z']
C = []
for i in A:
    for j in B:
        A.remove('c')
        B.remove('y')
        if i == 'a':
            B.remove('x')
        else:
    C.append((i, j)) 
print(C)
