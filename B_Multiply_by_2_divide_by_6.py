t=int(input())
for _ in range(t):
    n=int(input())
    a = n
    ans=0
    while a//3 > 0:       
        if a%6!=0:
            if (a*2)%6==0:
                ans+=1
                a=a*2
            else:
                break
        a//=6
        ans+=1
    
    if a==1:
        print(ans)
    
    else:
        print(-1)