from collections import Counter

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ac=Counter(a)
bc=Counter(b)
ans=0
for c in ac.keys():
    if c in bc.keys():
        ans+=ac[c] * (bc[c])
        
print(ans)