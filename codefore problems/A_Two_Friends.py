
t = int(input())
 
for _ in range(t):
    n= int(input())
    p = list(map(int,input().split()))
    con= False
    _map = {}
    for i in range(n):
        _map[i+1]=p[i]
    

    for k,v in _map.items():
        #print(_map[k],_map[v])
        if k == _map[v] :
            
            con = True
            break
    if con: 
        print(2)
    else:
        print(3)
    
    
    
