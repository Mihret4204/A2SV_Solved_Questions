from math import ceil
n,m,a=map(int,input().split())
r= ceil(n/a)
c = ceil(m/a)

print(r*c)