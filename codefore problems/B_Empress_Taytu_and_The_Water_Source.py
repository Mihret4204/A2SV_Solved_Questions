t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    def possible(s):
        total = 0
        for i in range(n):
            trips = (d[i] + s - 1) // s
            total += trips * a[i]
            if total > k:
                return False
        return True

    lo, hi = 1, max(d)
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)