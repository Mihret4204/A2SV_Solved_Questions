n = int(input())
s = []
for i in range(n):
    con = True
    j = '1'
    a = input()
    print(a)
    if a not in s:

        s.append((a,1))
        continue
    while a in s:
        if a not in s:
            break
        a+=j
        j=str(int(j)+1)
    s.append((a,0))
        
for i,j in s:
    
    if j==1:
        print(i)
    else:
        print(99)