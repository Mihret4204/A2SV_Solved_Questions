t=int(input())

for _ in range(t):
    n=int(input())
    ans=[]
    m=1

    while n>0:
        r=n%10
        n//=10   
        if r!=0:            
            ans.append(r*m)
        m*=10

    print(len(ans))
    print(*ans)