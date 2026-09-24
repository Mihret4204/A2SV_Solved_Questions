class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            s=0
            while x>0:
                r=x%10
                s+=r
                x//=10
            

            if s==i:
                return i
        return -1 