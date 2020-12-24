def age_is(n):
    if n == 1:
        return 10
    else:
        return age_is(n-1) + 2

print(age_is(5))