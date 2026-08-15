class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        n=len(nums)
        if all(i==0 for i in nums):
            return 0
        temp = nums[0]
        for i in range(1,n):   
            temp ^=nums[i]
        if temp==0:
            return n-1
       
           
        return n