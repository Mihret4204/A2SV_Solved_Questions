t=int(input())

for _ in range(t):
    l=int(input())
    n=input()

    
    ae,ao=0,0
    be,bo=0,0
    i=1
    while i<l+1:
        if (i-1)%2 ==1 and (int(n[i-1]))%2==0:
            be+=1
        if (i-1)%2 ==1 and (int(n[i-1]))%2!=0:
            bo+=1
        if (i-1)%2 ==0 and (int(n[i-1]))%2==0:
            ae+=1
        if (i-1)%2 ==0 and (int(n[i-1]))%2!=0:
            ao+=1
        i+=1
    if l%2==0:
        if be>0:
            print(2)
        else:
            print(1)
    else:
        if ao>0:
           
            print(1)
        else:
            
            print(2)
        
        
























        
        
    
    