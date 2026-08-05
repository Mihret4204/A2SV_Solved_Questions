class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if int(s[-1]): 
            return False
        dp = [False] * n
        dp[0] = True
        r, maxR = 0,maxJump
        for i in range(minJump, n):
            if i > maxR: 
                return False
            r += dp[i - minJump]
            if i > maxJump:
                r -= dp[i - maxJump - 1]
            if r and not int(s[i]):
                dp[i] = True
                maxR = i + maxJump

        return r > 0