class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        z=0
        ans=0
        if nums[0]==0:
            z+=1
        r=1
        while r<len(nums):
            if nums[r]==0:
                z+=1
            
            while z>1:
                if nums[l]==0:
                    z-=1
                l+=1
            ans=max(ans,r-l)
            r+=1
        return ans