import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1

    freq = {}
    for i in range(1, n + 1):
        d = deg[i]
        freq[d] = freq.get(d, 0) + 1

    leaf_count = freq.get(1, 0)

    x = 0
    for d in freq:
        if d > 1:
            x = max(x, freq[d])

    y = leaf_count // x

    print(x, y)