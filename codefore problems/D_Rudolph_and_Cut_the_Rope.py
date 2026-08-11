t = int(input())

for _ in range(t):
    n= int(input())
    ans=0
    for _ in range(n):
        x,y=map(int,input().split())
        if x >y:
            ans+=1
    print(ans)