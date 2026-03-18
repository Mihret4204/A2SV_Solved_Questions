n,m=map(int,input().split())
arr=list(map(int,input().split()))
a=[]
if n==m:
    print(0)
elif m==1:
    print(max(arr)-min(arr))
else:
    for i in range(n-1):
        a.append(arr[i+1]-arr[i])
    a.sort()
    print(sum(a[:n-m]))

    

