import sys
sys.setrecursionlimit(10000)
arr = list(map(int,input().split()))

n=arr[0]
memo = [-2]*(n+1)
memo[0]=0 
a,b,c = arr[1],arr[2],arr[3]
def dp(i):
    
    if memo[i]!=-2:
        return memo[i]
    x,y,z = -1,-1,-1
    if i-a>=0 :
        if dp(i-a) != -1:
            x = dp(i-a) + 1
        
    if i-b>=0:
        if dp(i-b) != -1:
            y = dp(i-b) + 1
       
    if i-c >=0:
        if dp(i-c) != -1:
            z = dp(i-c) + 1

    ar = []
    if x!=-1:
        ar.append(x)
    if y!=-1:
        ar.append(y)
    if z!=-1:
        ar.append(z)
    if ar:
        memo[i]=max(ar)
    else:
        memo[i]=-1

    return memo[i]
    
dp(n)

print(memo[n])
