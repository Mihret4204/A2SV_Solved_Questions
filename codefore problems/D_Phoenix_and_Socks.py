import sys
from collections import Counter


data = sys.stdin.read().split()
idx = 0
t = int(data[idx])
idx += 1

for case in range(t):
    n = int(data[idx])
    left_num = int(data[idx+1])  # l
    right_num = int(data[idx+2])  # r
    idx += 3
    
    c = [int(data[idx + i]) for i in range(n)]
    idx += n
    
    L = [0] * (n + 1)
    R = [0] * (n + 1)
    
    for i in range(left_num):
        L[c[i]] += 1
    for i in range(left_num, n):
        R[c[i]] += 1
    
    common = 0
    for i in range(1, n + 1):
        common += min(L[i], R[i])
    
    k = abs(left_num - right_num) // 2
    if k == 0:
        print(n // 2 - common)
        continue
    
    gain = 0
    if left_num > right_num:
        
        for i in range(1, n + 1):
            if L[i] > R[i]:
                ex = L[i] - R[i]
                gain += ex // 2
    else:
        
        for i in range(1, n + 1):
            if R[i] > L[i]:
                ex = R[i] - L[i]
                gain += ex // 2
    
    added = min(k, gain)
    max_free = common + added
    recolors = n // 2 - max_free
    ans = k + recolors
    print(ans)