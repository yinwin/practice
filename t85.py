n = int(input('input a odd number:\n'))
class MyNumbers:
    def __iter__(self):
        self.a = 10
        return self
    def __next__(self):
        x = self.a - 1
        self.a *=10
        return x
myclass = MyNumbers()
myiter = iter(myclass)
i = 1
while i < 2:
    j = next(myiter)
    if j % n != 0:
        i=1
    else:
        print(j)
        i +=1
'''
def my_numbers():
    a = 10
    while True:
        
        n = a-1
        a = a * 10
        yield n

f = my_numbers()
m = int(input('input a odd number:\n'))
i = 1
while i < 2:
    j = next(f)
    if j % m != 0:
        j += 1
    else:
        print(j)
        i += 1
'''