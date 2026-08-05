import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    ans = float('inf')

    for k in range(34):  
        
        nb = b + k
        if nb == 1:
            continue
        cur_a = a
        ops = k
        while cur_a > 0:
            cur_a //= nb
            ops += 1

        ans = min(ans, ops)

    print(ans)