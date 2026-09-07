class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        preMax = []
        sufMin = []
        mx = nums[0]
        mi = nums[-1]
        for i in range(n):
            mi = min(mi,nums[n-i-1])
            mx = max(mx, nums[i])
            preMax.append(mx)
            sufMin.append(mi)
        
        ans = -1
        for i in range(n):
            if preMax[i]-sufMin[n-i-1]<=k:
                ans = i
                break
        return ans