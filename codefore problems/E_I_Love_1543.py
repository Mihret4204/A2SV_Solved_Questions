t=int(input())
for _ in range(t):
    rows,cols=map(int,input().split())
    mat=[input() for _ in range(rows)]
    
    ans=0
    i=0
    
    while i<rows//2 and i<cols//2:
        chars=[]
        #top->right->bottom->left
        for c in range(i,cols-i):
            chars.append(mat[i][c])
        for r in range(i+1,rows-1-i):
            chars.append(mat[r][cols-1-i])
        for c in range(cols-1-i,i-1,-1):
            chars.append(mat[rows-1-i][c])
        for r in range(rows-2-i,i,-1):
            chars.append(mat[r][i])
        
        
        s="".join(chars)
        s+=s[:3]
        ans+=s.count("1543")

        i+=1
    print(ans)

