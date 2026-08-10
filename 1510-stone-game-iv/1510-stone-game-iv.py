class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mx = 10**5 
        memo = [False]*(mx+1)

        def dp():
            for i in range(mx+1):
                if memo[i]==True:
                    continue
                for j in range(1,isqrt(mx-i)+1):
                    memo[i+j**2]=True

        dp()
        print(memo[1])
        return memo[n]