t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    con=True
    z,o=0,0
    for i in a:
        
        if i=='0':
            z+=1
        else:
            o+=1
            
    #print(z,o)
    if a==b:
        print("YES")
        continue
    if n%2==1 and a!=b:
        print("NO")
        continue

    for r in range(n-1,-1,-2):
        print(o,z)
        if a[r]==b[r] and a[r-1]==b[r-1]:
            if (a[r]=='0' and a[r-1]=='1') or (a[r]=='1' and a[r-1]=='0'):
                z-=1
                o-=1
            elif a[r]=='0':
                z-=2
            else:
                o-=2
          
        elif (a[r]!=b[r] and a[r-1]!=b[r-1]):
            if z!=o:
                #print(99)
                con=False
                break
            else:
                if a[r]== a[r-1]:
                    if a[r]=='0':
                        z-=2
                    else:
                        o-=2
                else:
                    z-=1
                    o-=1
                pass
        elif ((a[r]!=b[r] and a[r-1]==b[r-1]) or (a[r]==b[r] and a[r-1]!=b[r-1])):
            con=False
            break

            
            
    if con==True:
        print("YES")
    else:
        print("NO")