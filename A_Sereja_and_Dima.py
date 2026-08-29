t = int(input())
arr=list(map(int,input().split()))

a,b = 0,0
i,j = 0,t-1
con=True
while i<=j:
    if arr[i]>arr[j]:
        if con:
            a+=arr[i]
            
        else:
            b+=arr[i]
        i+=1
        
    else:
        if con:
            a+=arr[j]
        else:
            b+=arr[j]
        j-=1
    con = not con
print(a,b)
