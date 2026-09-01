t = int(input())
for i in range(t):
    n = int(input())
    arr=list(map(int,input().split()))
    _map={}
    for i in range(3):
        _map[arr[i]]=_map.get(arr[i],0)+1
    ans = -1
    num = -1
    for k,val in _map.items():
        if val<2:
            ans = k
        else:
            num= k

    if ans==-1:
        s=set(arr)
        for c in s:
            if c == num:
                continue
            else:
                ans = c
    print(arr.index(ans)+1)
    