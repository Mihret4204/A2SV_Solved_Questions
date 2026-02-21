t=int(input())

for _ in range(t):
    casino=[]
    n,k=map(int,input().split())
    for i in range(n):
        l,r,real=map(int,input().split())
        casino.append([l,r,real])
    casino=sorted(casino, key=lambda x: x[2])
    curr=k
    count=0
    for i in range(len(casino)):

        if casino[i][0]<=curr<=casino[i][2]:
            curr=casino[i][2]
        else:
            continue
    print(curr)
