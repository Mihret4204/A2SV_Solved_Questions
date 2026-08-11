s=input()
arr=[]
for c in s:
    if c=="+":
        continue
    arr.append(c)
arr.sort()
ans=""
ans=arr[0]
for i in range(1,len(arr)):
    ans=ans+"+"+arr[i]
print(ans)
    