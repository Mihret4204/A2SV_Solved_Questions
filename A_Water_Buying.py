t = int(input())

for _ in range(t):
    n , a, b= map(int, input().split())
    if n %2==0:
        x=(n//2)*b
    else:
        x=(n//2)*b + a
    y=n*a
    ans=min(x,y)
    print(ans,)