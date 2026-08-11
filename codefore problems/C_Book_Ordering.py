t=int(input())
arr=[]
for _ in range(t):
    w,h=map(int,input().split())
    arr.append([w,h])
case=True
prev=max(arr[0][0],arr[0][1])
for i in range(t-1):
    if arr[i+1][0]<=prev and arr[i+1][1]<=prev:
        prev=max(arr[i+1][0],arr[i+1][1])
    elif arr[i+1][0]<=prev and arr[i+1][1]>prev:
        prev=arr[i+1][0]
    elif arr[i+1][1]<=prev and arr[i+1][0]>prev:
        prev=arr[i+1][1]
    else:
        case=False
if case:
    print("YES")
else:
    print("NO")
