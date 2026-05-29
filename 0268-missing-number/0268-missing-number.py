class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = 0
        for i in range(len(nums)): 
            ans ^= nums[i]
            n  ^= i    
        n^=(len(nums))
        return ans ^ n