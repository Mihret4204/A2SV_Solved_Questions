s=input()
arr=[]
con=False
a=['H','Q','9','+']
for i in s:
    arr.append(i)
for c in arr:
    if c in a:
        con=True
        break
if con:
    print('YES')
else:
    print('NO')