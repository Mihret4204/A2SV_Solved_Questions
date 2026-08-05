class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(i,buy):
            if i >= n:
                return 0
            
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy:
                buying = dp((i+1),not buy) - prices[i]
                cooldown = dp(i+1,buy)
                memo[(i,buy)] = max(buying,cooldown)
            else:
                selling = dp((i+2),not buy) + prices[i]
                cooldown = dp(i+1,buy)
                memo[(i,buy)] = max(selling,cooldown)
            return memo[(i,buy)]


        return dp(0,True)