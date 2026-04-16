t=int(input())

for _ in range(t):
    n,h=map(int,input().split())
    ans=0
    for i in range(n):
        l,w=map(int,input().split())
        ans+=max(l,w)
    if ans>=h:
        print('YES')
    else:
        print('NO')