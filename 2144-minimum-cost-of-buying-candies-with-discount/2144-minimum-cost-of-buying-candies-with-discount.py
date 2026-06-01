class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n =  len(cost)
        ans =  sum(cost)
        for i in range(n-1,-1,-1):
            if (n-i)%3 == 0:
                ans-=cost[i]
        
        return ans