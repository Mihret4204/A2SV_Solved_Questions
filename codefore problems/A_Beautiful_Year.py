y=int(input())
con=True

while con:
    y+=1
    x=str(y)
    if x[1]!=x[2] and x[1]!=x[3] and x[1]!=x[0] and x[2]!=x[3] and x[2]!=x[0] and x[3]!=x[0]:
        con=False     
print(y)

