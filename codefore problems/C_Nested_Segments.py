n=int(input())
list1=[]
con=True
for i in range(n):
    l,r=map(int,input().split())
    list1.append([l,r,i])
list1=sorted(list1,key=lambda x: (x[0] ,-x[1]))

max_r=-1
idx=-1
for l,r,i in list1:
    if r<=max_r:
        print(i+1,idx+1)
        con=False
        break
    else:
        max_r=r
        idx=i
if con:
    print(-1,-1)

    


    