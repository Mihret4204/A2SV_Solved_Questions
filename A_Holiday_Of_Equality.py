n = int(input())
arr = list(map(int,input().split()))
mx = max(arr)
ans= 0
for i in range(n):
    ans+=(mx-arr[i])
print(ans)