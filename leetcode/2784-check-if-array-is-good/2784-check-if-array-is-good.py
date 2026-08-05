class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums)<2:
            return False
        if n!=len(set(nums)) :
            return False
        nums.sort()
        if nums[-1]!=nums[-2]:
            return False
        
        for i in range(len(nums)-2):
            if nums[i] == nums[i+1]:
                return False
        return True
