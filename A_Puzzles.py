n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

ans = arr[n-1]-arr[0]
for r in range(n,m): 
    
    ans=min(ans, arr[r]-arr[r-n+1])
print(ans)