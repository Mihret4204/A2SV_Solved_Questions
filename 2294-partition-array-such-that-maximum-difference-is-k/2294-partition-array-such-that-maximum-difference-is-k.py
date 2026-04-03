class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=1
        a=nums[0]

        for i in range(1,len(nums)):
            
            if nums[i]-a>k:
                ans+=1
                a=nums[i]
            
        return ans


            

            
            
