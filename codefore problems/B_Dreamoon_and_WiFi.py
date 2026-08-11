from math import factorial
a=input()
b=input()

x=0
for c in a:
    if c=='+':
        x+=1
    else:
        x-=1
w,y,u=0,0,0
for c in b:
    if c=='+':
        u+=1
        w+=1
    elif c=='-':
        w-=1
    else:
        y+=1
if w==x and y==0:
    print(float(1))
else:
    print(y,u)
    ans=factorial(y)/(factorial(y-u)*factorial(u))

    #print(1/ans)