class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        x=nums[n-1]
        for i in range(n-2,-1,-1): 

            #print(nums[i],x)
            if nums[i]>x:
                #print(nums[i],x)
                t=nums[i]//x
                if nums[i]%x:
                    t+=1
                x=nums[i]//t
                ans+=t-1
            else:
                x=nums[i]
        return ans
