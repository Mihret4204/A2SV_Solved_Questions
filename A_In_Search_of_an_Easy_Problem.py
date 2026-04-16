t=int(input())
arr=list(map(int,input().split()))
con=True
for n in arr:
    if n==1:
        con=False
        break
if con:
    print('EASY')
else:
    print('HARD')