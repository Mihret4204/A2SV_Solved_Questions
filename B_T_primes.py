from math import isqrt
t=int(input())
arr=list(map(int,input().split()))
for n in arr:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
        if c>3:
            break
    
    if c==3:
        print('YES')
    else:
        print('NO')