t=int(input())
for _ in range(t):
    n,k=map(int,input().split())

    arr=list(map(int,input().split()))
    pos=list(map(int,input().split()))

    _map=[]
    for i in range(n):
        _map.append((abs(pos[i]),arr[i]))
    _map.sort()

    total=0
    con=True

    for d,val in _map:
        total+=val
        if total>d*k:
            con=False
            break
    if con:
        print('YES')
    else:
        print('NO')
         
         