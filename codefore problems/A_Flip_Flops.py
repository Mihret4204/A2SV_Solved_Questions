t=int(input())
for _ in range(t):
    n,c,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    
    for i in range(n):
        if c<arr[i]:
            break
        elif  k>0 :
            a=min(k,c-arr[i])
            k=k-a
            c=c+a+arr[i]
           
        elif arr[i]<=c:
            c+=arr[i]
            
    print(c)