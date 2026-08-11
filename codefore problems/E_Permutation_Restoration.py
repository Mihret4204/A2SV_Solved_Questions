import sys
from heapq import heappush, heappop

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    intervals = []
    for i, bi in enumerate(b, start=1):
        if bi == 0:
            L = i + 1
            R = n
        else:
            L = i // (bi + 1) + 1
            R = i // bi

        intervals.append((L, R, i - 1))
    intervals.sort()
    ans = [0] * n
    pq = []
    j = 0
    for value in range(1, n + 1):
        while j < n and intervals[j][0] <= value:
            L, R, idx = intervals[j]
            heappush(pq, (R, idx))
            j += 1
        R, idx = heappop(pq)
        ans[idx] = value
    print(*ans)