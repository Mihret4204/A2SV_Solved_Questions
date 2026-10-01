n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
arr = []
x = 0
for c in a:
    x+=c
    arr.append(x)

for c in b:
    l = 0
    r = len(arr)-1
    
    while l<r:
        
        mid = l+(r-l)//2
        
        if  c<=arr[mid]:
            r=mid
        else:
            l=mid+1
    print(l+1)

