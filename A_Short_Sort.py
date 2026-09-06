n = int(input())

for _ in range(n):
    s  = input()
    if s[0]=='a' or s[-1]=='c' or s[1]=='b':
        print('YES')
    else:
        print('NO')