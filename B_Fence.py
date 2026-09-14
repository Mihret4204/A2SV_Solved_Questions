n,k = map(int,input().split())
arr = list(map(int,input().split()))
i= 0
s = sum(arr[:k])
ans = 1
a = s

for j in range(k,n):
    
    a = a-arr[i]+arr[j]
    
    if a<s:
        ans = i+2
        s = a
    i+=1
   
print(ans)