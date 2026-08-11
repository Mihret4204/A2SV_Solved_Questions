n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x=x[1:]
y=y[1:]
con=True
for k in range(1,n+1):
    if k  in x or k in y:
        continue
    else:
        con=False
        break
if con:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
