class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1]*n
        memo[0],memo[1]=cost[0],cost[1]


        def dp(i):
            if memo[i]!=-1:
                return memo[i]
            else:
                memo[i] = min(dp(i-1),dp(i-2))+cost[i]
                return memo[i]
        
        dp(n-1)
     
        return min(memo[-1],memo[-2])
        