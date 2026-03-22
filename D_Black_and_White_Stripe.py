t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=input()
    b=0
    for i in range(m):
        if s[i]=="B":
            b+=1
    ans=m-b  
    for r in range(m,n):
        if s[r]=="B":
            b+=1
        if s[r-m]=="B":
            b-=1
        ans=min(ans,m-b)
    print(ans)




        
