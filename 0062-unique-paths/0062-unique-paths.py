class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0]*n for j in range(m)]
        def dp(i,j):
            if i == 0 and j==0:
                memo[i][j]=1
                
            elif i==0 or j==0:
                memo[i][j]=1
                
            else:
                memo[i][j]= memo[i-1][j]+memo[i][j-1]
            return 
        for i in range(m):
            for j in range(n):
                dp(i,j)
        ans = (memo[m-1][n-1])
        return ans