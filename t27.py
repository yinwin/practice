def output(s,l):
    if l == 0:
        return s
    print(s[l-1],end = '')
    output(s,l-1)
s = input('Input a string:')
l = len(s)
output(s,l)