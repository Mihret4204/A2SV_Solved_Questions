k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
s = set()
mi = min(k,l,m,n)
mx = d//mi 

for i in range(1,mx+1):
   
    if i*k<=d:
        s.add(i*k)
    if i*l<=d:
        s.add(i*l)
    if i*m<=d:
        s.add(i*m)
    if i*n<=d:
        s.add(i*n)
print(len(s))