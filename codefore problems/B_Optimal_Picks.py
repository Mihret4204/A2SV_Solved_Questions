t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)

    ans=0
    for i in range(n):
        if i%2==0:
            ans+=arr[i]
        else:
            ans-=arr[i]
   
    

    for i in range(1,n,2):
        d=arr[i-1]-arr[i]
        m=min(d,k)
        arr[i]+=m
        k-=m
        ans-=m
        if k==0:
            break
   
    print(ans)