l = [1,1]
print([1])
print(l)
for i in range(2,10):
    
    m = [1]
    for j in range(i-1):
        # print(l[j+1])
        l[j] = l[j] +l[j+1]
    l = m + l 
    print(l)


    