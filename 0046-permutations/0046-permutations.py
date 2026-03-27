class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        
        def perm(i):
            if i==len(nums):
                ans.append(nums[:])
                return 
            for j in range(i,len(nums)):
                nums[j],nums[i]= nums[i],nums[j]
                perm(i+1)
                nums[j],nums[i]= nums[i],nums[j]  
        perm(0)
        return ans

            