class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        pre=0
        for n in nums:
            if n==0:
                pre=0
            else:
                pre+=1
            ans = max(ans,pre)
            
        return ans