
t = int(input())
for _ in range(t):
    x,y,n = map(int,input().split())
    
    k = n//x
    ans = k*x+y
    if ans>n:
        print(ans-x)
    else:
        print(ans)
            
       