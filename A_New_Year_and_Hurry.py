n, k = map(int,input().split())
m = 240-k
ans = 0

for i in range(n,-1,-1):
     
    x = 5*((i*(i+1))//2)
   
    if x<=m:        
        ans = i
        break
print(ans)
