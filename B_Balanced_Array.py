t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    if n%4==0:
        print('YES')
        x = 2
        y = 1
        for i in range(n//2-1):          
           
           a.append(x)
           b.append(y)
           x+=2
           y+=2
        a.append(x)
        b.append(y+n//2)
        

        print(*a,*b)      
    else:
        print('NO')
    