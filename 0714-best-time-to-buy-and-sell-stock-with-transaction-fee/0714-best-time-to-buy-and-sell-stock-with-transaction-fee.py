class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans = 0
        pr = prices[0]
        for i in range(1,len(prices)):
            if pr > prices[i]:
                pr = prices[i]
            elif  prices[i] >  pr + fee:
                ans = ans + prices[i] - pr -fee
                pr =prices[i] - fee
        return ans