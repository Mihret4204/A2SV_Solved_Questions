
n = int(input())

_map = {}
_mapp = {}
ans = 0
for i in range(n):
    a,b = map(int,input().split()) 
    
    x = _mapp.get(a,0)
    ans+= x
    y = _map.get(b,0)  
    ans+=y   
    _map[a]=_map.get(a,0)+1
    _mapp[b] =_mapp.get(b,0)+1
print(ans)