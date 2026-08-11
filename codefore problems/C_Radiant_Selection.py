from math import isqrt
t=int(input())

for _ in range(t):
    k=int(input())
    l,r=1,2*k
    while l<r:
        mid=l+(r-l)//2
        
        if mid-isqrt(mid)>=k:
            r=mid
        else:
            l=mid+1
    print(l)
        
    
        