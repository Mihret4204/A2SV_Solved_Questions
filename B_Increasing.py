t = int(input())
for _  in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    a = list(set(arr))
    a.sort()
    arr.sort()
    if arr==a:
        print('YES')
    else:
        print('NO')