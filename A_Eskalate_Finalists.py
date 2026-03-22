t=int(input())
arr=list(map(int,input().split()))
m=max(arr)
if m-25<=0:
    print(0)
else:
    print(m-25)