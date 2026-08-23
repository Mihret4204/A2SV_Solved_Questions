from decimal import Decimal, getcontext
n,l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = arr[0]
for i in range(1,n):
    a=Decimal(arr[i])
    b = Decimal(arr[i-1])
    ans = max(ans,((a-b)/2))
ans = max(ans,l-arr[-1])
print((ans))