t=int(input())

for _ in range(t):
    s=input()
    l=len(s)
    n=str(314159265358979323846264338327)
    n=n[:l]
    ans=0
    
    for i in range(l): 
        if s[i]!=n[i]:
            break
        ans+=1
    print(ans)
    
        