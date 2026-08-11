t=int(input())
for _ in range(t):
    n=int(input())
    red=list(map(int,input().split()))
    m=int(input())
    blue=list(map(int,input().split()))

    curr=0
    rm,bm=0,0
    for i in red:
        curr+=i
        rm=max(curr,rm)
    curr=0
    for j in blue:
        curr+=j
        bm=max(curr,bm)
    print(rm+bm)
    