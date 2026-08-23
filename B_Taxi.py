from math import ceil
n = int(input())
ans = 0
o = 0
t = 0
r = 0
arr = list(map(int,input().split()))
_map = [0]*5
for a in arr:
    _map[a]+=1
ans = _map[4]
_map[1] = max(0,_map[1]-_map[3])
ans+= _map[3]
ans+=(_map[2]//2)
if _map[2]%2 ==1:
    _map[1]=max(0,_map[1]-2)
    ans+=1
ans+=(ceil(_map[1]/4))
print(int(ans))
