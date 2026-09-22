from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    _map = defaultdict(list)
    for i in range(n):
        _map[i].append(n-i)
    print(_map)
    print(ans)