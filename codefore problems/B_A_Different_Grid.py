t=int(input())

for _ in range(t):
    r,c=map(int,input().split())
    arr=[]
    for i in range(r):
        arr.extend(map(int,input().split()))

    k=c*r

    if k<=1:
        print(-1)
        continue
    messed=arr[1:]+[arr[0]]

    i=0

    for _ in range(r):
        row=[]
        for j in range(c):
            row.append(str(messed[i]))
            i+=1
        print(" ".join(row))