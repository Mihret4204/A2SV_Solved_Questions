from math import ceil
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    ans = ceil((abs(a-b))/10)
    print(ans)