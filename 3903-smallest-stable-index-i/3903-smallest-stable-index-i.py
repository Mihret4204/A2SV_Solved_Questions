class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mi,mx = float('inf'), float('-inf')
        n=len(nums)
        a = -1
        
        for i in range(1,n+1):
          
            mi = min(nums[i-1:])
            mx = max(nums[:i])

            if mx-mi<=k:
              
                a = i-1
                break
                

        return a