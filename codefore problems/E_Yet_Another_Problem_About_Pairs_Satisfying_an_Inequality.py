from bisect import bisect_left

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    good = []
    ans = 0

    for j in range(1, n + 1):
        if a[j-1] < j:
            pos = bisect_left(good, a[j-1])
            ans += pos
            good.append(j)

    print(ans)