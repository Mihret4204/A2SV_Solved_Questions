import sys
import bisect

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    N = 1 << n

    for i in range(1, n+1):
        sz = 1 << i
        hf = sz >> 1

        for g in range(0, N, sz):
            l = a[g:g+hf]
            r = a[g+hf:g+sz]

            ls = sorted(l)
            rs = sorted(r)

            for j in range(hf):
                w = bisect.bisect_left(rs, l[j])
                a[g+j] += w

            for j in range(hf):
                w = bisect.bisect_left(ls, r[j])
                a[g+hf+j] += w

    print(*a)