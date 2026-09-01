from math import ceil
n,m,a,b = map(int,input().split())
x = ceil(n/m) * b
v = n//m
y = (n- v*m)*a +  v*b
z = n*a

ans = min(x,y,z)
print(ans)