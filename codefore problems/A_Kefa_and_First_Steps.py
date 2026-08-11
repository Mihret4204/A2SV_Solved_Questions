n=int(input())
arr=list(map(int,input().split()))

c=1
ans=0
for i in range(n-1):
    if arr[i]<=arr[i+1]:
        c+=1
    else:
        ans=max(c,ans)
        c=1
ans=max(ans,c) 
print(ans)