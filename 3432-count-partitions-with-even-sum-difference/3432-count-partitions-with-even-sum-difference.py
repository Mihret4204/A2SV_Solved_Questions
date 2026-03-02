class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        left=0
        right =sum(nums)
        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if (right -left)%2==0:
                count+=1
        return count