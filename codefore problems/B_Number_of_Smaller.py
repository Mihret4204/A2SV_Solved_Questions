n,m =map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ans=[]
for i in arr2:
    c=0
    for j in range(len(arr1)):
        if arr1[j]<i:
            c+=1
    ans.append(c)
print(*ans)
    