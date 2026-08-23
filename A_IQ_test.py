n = int(input())
arr = list(map(int,input().split()))
ev = {}
od = {}
for i in range(3):
    if arr[i]%2==0:
        ev[i]=ev.get(i,0)+1
    else:
        od[i]=od.get(i,0)+1
        
if not od:
    for i in range(n):
        if arr[i]%2==1:
            print(i+1)
            break

elif not ev:
    for i in range(n):
            if arr[i]%2==0:
                print(i+1)
                break
else:
    if len(ev)==1:
        for i in ev.keys():
            print(i+1)
    if len(od)==1:
        for i in od.keys():
            print(i+1)