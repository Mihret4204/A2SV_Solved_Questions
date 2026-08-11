t=int(input())
ans=0
for _ in range(t):
    m,n=map(int,input().split())
    if n-m>1:
        ans+=1
print(ans)