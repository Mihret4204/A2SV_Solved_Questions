class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0,0]
        nums.sort()
        for i in range (1,n):
            if nums[i-1]==nums[i]:
                ans[0]=nums[i-1]
                break
        ans[1]=  ((n * (n+1) )//2) - sum(set(nums))
        return ans