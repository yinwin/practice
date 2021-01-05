'''
if __name__ == '__main__':
    n = 0
    p = input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)
'''

n = 0 
p = input('input a octal number:\n')
for i in range(1,len(p)+1):
    n = n + 8 ** (i-1) *int(p[-i])
print(n)