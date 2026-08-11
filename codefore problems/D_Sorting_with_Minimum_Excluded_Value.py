t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    ans=[]

    while True:

        s=set(arr)
        mex=0

        while mex in s:
            mex+=1
        if all(arr[i]<=arr[i+1] for i in range(n-1)):
                break
        if mex<n:
            arr[mex]=mex
            ans.append(mex)
        else:
            for i in range(n):
                if arr[i]!=i:
                    arr[i]=mex
                    ans.append(i)
                    break
    print(len(ans))
    if ans:
        print(*[i+1 for i in ans])
    