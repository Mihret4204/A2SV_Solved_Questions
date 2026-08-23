t = int(input())
arr = list(map(int,input().split()))
a = arr[0]
b = arr[0]
ans = 0
for i in range(1,t):
    if arr[i] > b:
        ans+=1
        b = arr[i]

    elif arr[i] < a:
        ans+=1
        a = arr[i]
print(ans)