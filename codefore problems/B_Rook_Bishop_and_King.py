rowi,coli,rowj,colj = map(int,input().split())

if rowi == rowj or coli == colj:
    rook =1
else:
    rook= 2
if (rowi+coli)%2 != (rowj+colj)%2:
    bis = 0
elif abs(rowi- rowj) == abs(coli - colj):
    bis = 1
else:
    bis = 2
k = max(abs(rowi-rowj), abs(coli-colj))
print(rook , bis , k)