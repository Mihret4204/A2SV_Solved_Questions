class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def possible(a):
            if a ==0:
                return False
            curr=0
            for c in candies:
                curr+=c//a
            print(curr,a)
            return curr>=k
                
        r=max(candies)
        l=1
        ans=0
        while l<=r:
            mid=l+(r-l)//2

            if possible(mid):
                l=mid+1
                ans=mid
            else:
                r=mid-1
        return ans