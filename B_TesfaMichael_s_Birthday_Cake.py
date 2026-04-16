n,m =map(int,input().split())
s=input()
arr=[]
for c in s:
    arr.append(ord(c)-96)
arr.sort()
#print(arr)
ans=0
r=0
total=0
for i in range(len(s)-m):  
    x=0
    j=i
    k=j+1
    while x<m and j<n-1 and k<n-1:
       
        if abs(arr[j]-arr[k])>1:
            if x==m-1:
                print(99)
                total+=arr[j]+arr[k]
                x+=1
                continue
            total+=arr[j]
            x+=1
            j+=1
            k=j+1
        k+=1
        print(total)
        
    
    ans=max(ans,total)
    total=0
print(ans)