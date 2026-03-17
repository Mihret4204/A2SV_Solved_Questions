from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    total=arr[0]
    arr.sort()
    res={}
    
    for i in range(1,n):
        rem=arr[i]-total
        if rem<=n:
            res[rem]=res.get(rem,0)+1
        total=arr[i]
    print(len(res))
    
