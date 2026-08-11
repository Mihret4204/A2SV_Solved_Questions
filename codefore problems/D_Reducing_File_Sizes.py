n,m=map(int,input().split())
pairs=[]
total=0
red=[]
for _ in range(n):
    a,b=map(int,input().split())
    total+=a
    red.append(a-b)

red.sort(reverse=True)

k=0
while total>m and k<n: 
    total-=red[k]
    k+=1
if k==n and total>m:
    print(-1)
else:
    print(k)
   

