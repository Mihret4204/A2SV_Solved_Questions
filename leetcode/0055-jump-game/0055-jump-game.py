class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jum=len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if i>=jum-nums[i]:
                jum=i      
        return jum==0
        
        
            

         