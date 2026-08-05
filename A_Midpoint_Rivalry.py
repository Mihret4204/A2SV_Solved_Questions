t=int(input())

for _ in range(t):
    a,x,y=map(int,input().split())
    mi=min(x,y)
    ma=max(x,y)
    
    if a<mi or a>ma:
        print('YES')
    else:
        print('NO')
