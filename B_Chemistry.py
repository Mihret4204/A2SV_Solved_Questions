t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    _map = {}
    for c in s:
        _map[c]=_map.get(c,0)+1
    x=0
    for i,val in _map.items():
        if val%2==1:
            x+=1
    if x-k>1:
        print('NO')
    else:
        print('YES')
