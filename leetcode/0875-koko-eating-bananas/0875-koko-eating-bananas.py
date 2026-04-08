class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def possible(n):
            t=0
            for p in piles:
                t+=ceil(p/n)
                if t>h:
                    return False
            return True

        r=max(piles)
        l=1
        ans=0
        while l<=r:

            mid=l+(r-l)//2
            if possible(mid): 
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans