t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans=0
    a=0
    for i in range(n):
        if arr[i]==0:
            a+=1
            ans=max(a,ans)
        else:
            
            a=0
    print(ans)