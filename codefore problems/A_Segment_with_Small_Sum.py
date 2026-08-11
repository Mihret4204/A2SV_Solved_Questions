t,m=map(int,input().split())
arr=list(map(int,input().split()))
res=arr[0]
l=0
ans=0
j=1
i=0
while j<len(arr):
    if res<=m:
        res+=arr[j]
        j+=1
        l+=1 
        ans=max(ans,l) 
    while res>m:
        res-=arr[i]
        i+=1
        l-=1
print(ans)
    