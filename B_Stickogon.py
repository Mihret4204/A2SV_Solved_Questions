from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=Counter(arr)
    ans=0
    for c in a.values():
        if c>=3:
            ans+=c//3
    print(ans)
