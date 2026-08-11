t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    maxA = a[-1]
    
    for i in range(n-2):
        x=a[i]
        for j in range(i+1,n-1):
            y=a[j]
            k=j+1
            
            while k<n and x+y+a[k]>maxA and x+y>a[k] :
                k+=1
            ans=ans+k-j-1
    print(ans)