n=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
a=0
i=0
arr.sort(reverse=True)
for n in arr:
    a+=n
    i+=1
    if a>total-a:
        break
print(i)
