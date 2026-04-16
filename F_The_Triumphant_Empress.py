import sys
input = sys.stdin.readline

def update(i, v, n, bit):
    while i <= n:
        bit[i] += v
        i += i & -i

def query(i, bit):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))

    prisoners = sorted((A[i], i+1) for i in range(n))

    queries = []
    for i in range(q):
        k, x = map(int, input().split())
        queries.append((x, k, i))

    queries.sort()

    bit = [0]*(n+1)
    ans = [0]*q

    p = 0
    for x, k, idx in queries:
        while p < n and prisoners[p][0] < x:
            update(prisoners[p][1], 1, n, bit)
            p += 1
        ans[idx] = query(k, bit)

    for v in ans:
        print(v)