t = int(input())
_map = {}
for _ in range(t):
    s = input()
    _map[s]=_map.get(s,0)+1
a = 0
ans = ''
for k,val in _map.items():
    if val>a:
        a = val
        ans=k
print(ans)