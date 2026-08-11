n,k=map(int,input().split())
arr=list(map(int,input().split()))
store={}
for i,val in enumerate(arr):
    store[i]=val
store=sorted(store.items(), key= lambda x : x[1])

ans=[]
total=0

i=0
while i<len(store):
    total+=store[i][1]
    
    if total<k:
        ans.append(store[i][0])
        i+=1
    elif total==k:
        ans.append(store[i][0])
        break
    else:
        break
    

print(len(ans))
print(*ans) 


