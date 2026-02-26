class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ans=sum(nums[:k])
        curr=ans
        for i in range(k,len(nums)):
            curr-=nums[i-k]
            curr+=nums[i] 
            ans=max(curr,ans)
            
        return ans/k