class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        suffix = sum(nums[1:])
        
        for i in range(n):
            if prefix == suffix:
                return i
            if i+1<n:
                prefix+=nums[i+1]
            else:
                prefix=0
            suffix-=nums[i]
        return -1