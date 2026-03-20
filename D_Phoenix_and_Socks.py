from collections import Counter
t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))
    
    ans=n//2
    cl=Counter(arr[:l])
    cr=Counter(arr[l:])

    ans=ans+ abs(n//2-l)
    #print(ans)
    for c in cr.keys():

        if c in cl.keys():   
            #print(cl[c],9)         
            ans=ans-min(cl[c],cr[c])
        
    for c in cl.keys():

        if c in cr.keys():   
            #print(cl[c],9)         
            ans=ans-min(cl[c],cr[c])
        
    #ans=ans+ abs(n//2-l)      
    
    print(ans)
