class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if i<len(nums) and nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        ans=[]
        for n in nums:
            if n!=0:
                ans.append(n)
        zeros=len(nums)-len(ans)
        ans=ans+[0]*zeros
        
        return ans

        