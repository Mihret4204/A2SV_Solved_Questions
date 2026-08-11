from math import ceil
t = int(input())
for _ in range(t):
    n,c,b = map(int,input().split())

    x = ceil(n/c)
    
    if n - x <= b:  
        print('NO')
    else: 
        print('YES')
