from collections import Counter
t=int(input())
for i in range(t):
    a=input()
    b=input()
    counta=Counter(a)
    countb=Counter(b)
    if counta-countb!={}:
        print("Impossible")
        break
    s=[]
    store=countb-counta
    for c in store.keys():
        x=c*(store[c])
        s.append(x)
    s.sort()
    ans="".join(s)
    
    i=0
    j=0
    res=""
    while i<len(ans) and j<len(a):
        if ans[i]>=a[j]:
            res+=a[j]
            j+=1
        else:
            res+=ans[i]
            i+=1
    if i<len(ans):
        res+=ans[i:]
    if j<len(a):
        res+=a[j:]
    print(res)
            
                

            
        
        

        
    
    