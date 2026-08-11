n = int(input())
arr = list(map(int,input().split()))

mi = min(arr)
mx = max(arr)
a,b = 0 ,0
for i in range(n):
    if arr[i]==mx:
        a = i
        break
for i in range(n-1,-1,-1):
    if arr[i]==mi:
        b = i
        break
if a <= b:
    print((n-b)+a-1)
else:
    print(a+ (n-b)-2)