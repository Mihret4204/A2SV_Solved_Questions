t=int(input())
arr=list(map(int,input().split()))
def dist():
    asum=sum(arr)
    ans=float('inf')

    def rec(i,total):
        nonlocal ans
        if i==t:
            ans=min(ans,abs(asum-2*total))
            return
       
        rec(i+1,total+arr[i])
        rec(i+1,total)

    rec(0,0)
    print(ans)
dist()
         