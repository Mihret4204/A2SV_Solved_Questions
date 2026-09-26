a = list(map(int,input().split()))
s=input()
ans=0
for c in s:
    x = int(c)
    ans+=a[x-1]
print(ans)