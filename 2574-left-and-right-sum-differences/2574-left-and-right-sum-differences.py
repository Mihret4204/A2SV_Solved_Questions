class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        pre = 0
        total = sum(nums) 
        for i in range(len(nums)):
            pre += nums[i]
            ans.append(abs(total-pre))
            total -= nums[i]
            
        return ans