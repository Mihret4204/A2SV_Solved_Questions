t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))
    curr=0
    win=0
    for x in arr:
        curr+=x
        
        if  l<=curr<=r:
            win+=1
            curr=0
        elif  curr>r :
            curr=x
            if  l<=curr<=r:
                win+=1
                curr=0
        
         
    print(win)