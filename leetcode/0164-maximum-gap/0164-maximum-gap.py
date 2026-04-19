class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        ans=0
        nums.sort()

        for i in range (1,len(nums)):
            ans=max((nums[i]-nums[i-1]),ans)
        return ans