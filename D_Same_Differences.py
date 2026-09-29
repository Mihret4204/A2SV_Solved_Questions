from collections import defaultdict
from math import comb
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    _map = defaultdict(list)
    for i in range(n):
        _map[i-arr[i]].append(i)
    ans = 0
    for i,val in _map.items():
        x = len(val)
        ans+=(x*(x-1))//2
    print(ans)
       
