n = int(input())
a = b = []
ans = 0
curr=0
for i in range(n):
    a,b= map(int,input().split())
    curr+= b -a 
    ans = max(ans,curr)
print(ans)