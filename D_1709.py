t=int(input())
for _ in range(t):
    n=int(input())
    ans=[]
    c=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    
    for i in range(n):
        if a[i]>b[i]:
            a[i],b[i]=b[i],a[i]
            ans.append([3,i+1])

    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                ans.append([1, i+1])
    
    
    for _ in range(n):
        for i in range(n-1):
            if b[i] > b[i+1]:
                b[i], b[i+1] = b[i+1], b[i]
                ans.append([2, i+1])
    
    

    print(len(ans))

    for x in ans:
        print(x[0],x[1])