t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans,a = 0 , 0
    for i in range(n):
        x = arr[i]-a
        a = arr[i]
        ans = max(ans,x)
    ans=max(ans,2*(k-arr[-1]))
    print(ans)