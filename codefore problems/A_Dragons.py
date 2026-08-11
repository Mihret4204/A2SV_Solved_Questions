s,n = map(int,input().split())

_map = []
for i in range(n):
    x,y = map(int,input().split())
    _map.append([x,y])

_map.sort(key=lambda x: x[0])
p = s
flag = True
for i in range(n):
    if p > _map[i][0]:
        p += _map[i][1]
       
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")