t=int(input())
for _ in range(t):
    n = int(input().strip())
    mat=[]
    ans=0
    for _ in range(n):
        row=input().strip()
        mat.append(row)
    for i in range((n+1)//2):
        for j in range(n//2):
            count=int(mat[i][j]) + int(mat[j][n-1-i]) + int(mat[n-1-j][i])+ int(mat[n-1-i][n-1-j])
            flip=min(count,4-count)
            ans+=flip
    print(ans)
