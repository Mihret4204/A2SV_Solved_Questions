arr = list(map(int,input().split()))
arr.sort()
ans = []
for i in arr[:-1]:
    ans.append(arr[-1]-i)
print(*ans)