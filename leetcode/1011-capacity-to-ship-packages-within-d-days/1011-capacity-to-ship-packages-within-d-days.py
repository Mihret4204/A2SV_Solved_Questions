class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def ispossible(n):
            day=1
            curr_sum=0
            for w in weights:
                curr_sum+=w

                if curr_sum>n:
                    day+=1
                    curr_sum=w

                    if day>days:
                        return False
            return True

        l=max(weights)
        r=sum(weights)
        ans=r
        while l<=r:
            mid=l+(r-l)//2

            if ispossible(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans