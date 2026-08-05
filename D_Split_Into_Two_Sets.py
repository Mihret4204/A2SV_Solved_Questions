from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    con = True

    for _ in range(n):
        a, b = map(int, input().split())
        if a == b:
            con = False
        g[a].append(b)
        g[b].append(a)
        deg[a] += 1
        deg[b] += 1

    for i in range(1, n + 1):
        if deg[i] != 2:
            con = False

    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] != -1:
            continue

        q = deque([i])
        color[i] = 0

        while q:
            u = q.popleft()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    con = False

    if con:
        print('YES')
    else:
        print('NO')