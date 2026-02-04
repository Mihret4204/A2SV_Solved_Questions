class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        loop=0
        for num in nums: 
            if loop!=num:
                return loop
            else:
                loop+=1        
        return loop