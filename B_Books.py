n,t = map(int,input().split())
arr =  list(map(int,input().split()))

i,j = 0,1
a = arr[0]
if arr[0]>t:
    ans=0
else:
    ans = 1
while j<n and j>=i:
    
    while j<n and a<t:
        a=a+arr[j]
        j+=1
    if a<=t: 
        ans = max(j-i,ans)
    else:
        ans= max(ans,j-i-1)
    
    a = a-arr[i]
    i+=1
print(ans)