class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float('inf')
        for n in nums:
            s=0
            while n > 0:
                s+=n%10
                n//=10
            ans=min(ans,s)
        
        return ans