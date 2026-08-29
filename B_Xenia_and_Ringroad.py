n,m = map(int,input().split())
arr=list(map(int,input().split()))
ans=0
curr=1
for i in range(m):
    
    if curr>arr[i]:
        ans+=(n-(curr-arr[i]))%n
    else:
        ans+=(arr[i]-curr)%n

    curr= arr[i]
    
print(ans)
