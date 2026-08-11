t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    ans=0
    for i in range(0,len(arr),2):
        ans+=(min(arr[i],arr[i+1]))
    print(ans)