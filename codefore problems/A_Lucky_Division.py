n=input()
con=False

def sol(n):

    for i in n:
        if i=='4' or i=='7':
            continue
        else:
            return False        
    return True


t=int(n)
j=1
while j<=int(n):
    
    if t%j==0 and sol(str(j)):
        con=True
        break
    j+=1
if con:
    print('YES')
else:
    print('NO')

