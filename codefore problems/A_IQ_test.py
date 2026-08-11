t=int(input())
arr=list(map(int,input().split()))

c={0:0,1:0}
o=0
for i in range(3):
    if arr[i]%2==1:
        o+=1
if o>1:
    for i in range(t):
        if arr[i]%2==0:
            print(i+1)
            break
else:
    for i in range(t):
        if arr[i]%2==1:
            print(i+1)
            break
