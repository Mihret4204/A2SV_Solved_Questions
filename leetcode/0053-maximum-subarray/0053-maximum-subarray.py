class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        total=nums[0]
        for num in nums[1:]:
            total=max(num,total+num)
            ans=max(total,ans)
        return ans