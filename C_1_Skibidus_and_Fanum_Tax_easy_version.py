t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))    

    def possible(x:int,y:int):
        mini=x
        for j in b:
            if j-x<=y and mini>j-x:
                mini=y-x
        if y>=mini:
            return True
        return False
    con=True
    c=0
    for i in range(len(a)-1):
        if a[i]<=a[i+1]:
            continue
        else:
            if c>0:
                con=False
                break
            elif possible(a[i],a[i-1]):
                c+=1
    if con:
        print('YES')
    else:
        print('NO')
            