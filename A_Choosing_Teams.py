n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans=0

for i in range(2,n,3):
    
    if arr[i]>5-k:
        break
    ans+=1
print(ans)