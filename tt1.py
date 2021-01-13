a='abcdada'
b='a'
c=[]
d=-1
while a.find(b) != -1:
    d += a.find(b)+1
    c.append(d)
    a = a[a.find(b)+1:]
    
print(c)
    
