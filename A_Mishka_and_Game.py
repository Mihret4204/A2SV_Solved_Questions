t = int(input())
c = m = 0
for _ in range(t):
    x,y = map(int,input().split())
    
    if x<y:
        c+=1
    elif x>y:
        m+=1
    else:
        c+=1
        m+=1
if m>c:
    print('Mishka')
elif m<c:
    print('Chris')
else:
    print('Friendship is magic!^^')