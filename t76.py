sum = 0


def sum_n(n):
    sum = 0
    for i in range(0, n, 2):
        if n % 2 == 0:
            sum = sum + 1/(i+2)
        if n % 2 == 1:
            sum = sum + 1/(i+1)
    print(sum)
sum_n(10)
