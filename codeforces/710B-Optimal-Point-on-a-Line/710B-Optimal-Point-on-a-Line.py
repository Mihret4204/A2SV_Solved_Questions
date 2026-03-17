n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if n%2==0:
    i=n//2-1
else:
    i=n//2
print(arr[i])