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
