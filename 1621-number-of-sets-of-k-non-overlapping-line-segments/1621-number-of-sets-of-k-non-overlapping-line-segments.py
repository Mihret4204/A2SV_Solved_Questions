class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        dp = [[0] * (k + 1) for _ in range(n)]
        # print(dp)
        for i in range(n):
            dp[i][0]=1
        # print(dp)
        for j in range(1,k+1):
            s = 0
            for i in range(1,n):
                s = (s+dp[i-1][j-1]) % (10**9 + 7)
                dp[i][j]=(dp[i-1][j]+s) % (10**9 + 7)
        return dp[n-1][k]