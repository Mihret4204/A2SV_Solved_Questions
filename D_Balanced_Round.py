t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    j = 0
    mx = 0
    for i in range(1,n):
        if arr[i]-arr[i-1]>m:
            mx=max(mx,i-j)
            j=i
       
    mx=max(mx,n-j)
    
    print(n-mx)
