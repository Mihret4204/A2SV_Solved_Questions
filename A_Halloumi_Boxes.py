t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    x = sorted(arr)
    if k==1 and x!=arr:
        print('NO')
    else:
        print('YES')
