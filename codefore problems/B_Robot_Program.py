m = int(input())    
for _ in range(m):
    n,x,t=map(int,input().split())
    s=input().strip()
    prefix=[0]*(n+1)
    step={'L':-1,'R':1}
    moves = {'L':-1, 'R':1}
    prefix = [0] * (n + 1)
    for i in range(n):
        c=s[i]
        prefix[i+1]=prefix[i]+moves[c]
    fz=-1
    for i in range(1,n+1):
        if prefix[i]+x==0:
            fz=i
            break
    if fz==-1 or fz>t:
        print(0)
        continue
    fr=-1
    for i in range(1,n+1):
        if prefix[i]==0:
            fr=i
            break
    if fr==-1:
        print(1)
        continue
    rem=t-fz
    remz=rem//fr
    print(remz+1) 
