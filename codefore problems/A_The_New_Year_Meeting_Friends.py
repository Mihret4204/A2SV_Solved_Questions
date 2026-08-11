from math import ceil
x,y,z=map(int,input().split)
s=x+y+z
if s%2==2:
    av=ceil(s/3)
else:
    av=s//3
ans=abs(x-av)+abs(y-av)+abs(z-av)

print(ans)
