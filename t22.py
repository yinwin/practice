A = ['a', 'b', 'c']
B = ['x', 'y', 'z']
C = []
for i in B:
    for g in B:
        if i != g:
            for q in B:
                if i !=q and g != q:
                    if i != 'x' and q != 'x' and q != 'z':
                        C = zip(A, (i, g, q))
                        print(list(C))

        
