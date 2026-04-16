from math import ceil
n,m=map(int,input().split())
r=ceil(n/2)
if m<=r:
    print(m*2-1)
else:
    print(2*(m-r))