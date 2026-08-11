n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for num in a :
    if num <= k:
        ans += 1
    else:
        ans += 2
print(ans)