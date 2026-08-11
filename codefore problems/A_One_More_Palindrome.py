from collections import Counter

t=int(input())
 
for _ in range(t):
    s=input()
    cs=Counter(s)
    even=0
    for i,val in cs.items():
        if val>=2:
            even+=1
        
    if even>=2:
        print("YES")
    else:
        print("NO")
    
