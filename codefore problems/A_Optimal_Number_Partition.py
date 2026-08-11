t=int(input())
arr=list(map(int,input().split()))
n=len(arr)
ans=0
arr.sort()
for i in range(n//2):
    x=arr[i]+arr[n-i-1]
    ans+=x**2
print(ans)