import sys
input = sys.stdin.readline
import bisect

INF = int(1e18)

def solve():
    n, m = map(int, input().split())
    va = list(map(int, input().split()))
    vb = list(map(int, input().split()))
    vb.sort()
    prev = -INF
    
    for i in range(n):
        options = []
        
        if va[i] >= prev:
            options.append(va[i])
    
        target = prev + va[i]
        idx = bisect.bisect_left(vb, target)
        
        if idx < m:
            val = vb[idx] - va[i]
            if val >= prev:
                options.append(val)
        
        if not options:
            print("NO")
            return
        
        prev = min(options) 
    
    print("YES")


t = int(input())
for _ in range(t):
    solve()