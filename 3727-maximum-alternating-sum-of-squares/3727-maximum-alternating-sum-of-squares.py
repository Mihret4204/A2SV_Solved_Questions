class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i]=abs(nums[i])
        nums.sort()
        x=n//2
        ans=0
        for i in range(n//2):
            a=nums[i+x]**2
            a-=nums[i]**2
            ans+=a
        if n%2==0:
            return ans
        
        return ans+nums[-1]**2