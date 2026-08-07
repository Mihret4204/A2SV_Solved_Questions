class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1]*n

        def dp(i):
            if i==0:
                return cost[0]
            elif i==1:
                return cost[1]
            elif memo[i]!=-1:
                return memo[i]
            else:
                memo[i] = min(dp(i-1),dp(i-2))+cost[i]
                return memo[i]
        
        dp(n-1)
        
        return min(dp(n-1),dp(n-2))