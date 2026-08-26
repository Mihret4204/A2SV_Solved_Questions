t = int(input())
for i in range(t):
    n =  int(input())
    arr =  list(map(int,input().split()))
    arr.sort()
    con = True
    for i in range(1,n):
        if arr[i]-arr[i-1]>1:
            con =False
            break
    if con:
        print('YES')
    else:
        print('NO')
        