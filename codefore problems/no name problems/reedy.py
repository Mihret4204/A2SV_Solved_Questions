num=int(input("Enter a number: "))

arr=[25,15,5,1]
ans={}
i=0
while i<len(arr) and num!=0:
    q=num//arr[i]
    num=num%arr[i]
    ans[arr[i]]=q
    i+=1
print(ans)
