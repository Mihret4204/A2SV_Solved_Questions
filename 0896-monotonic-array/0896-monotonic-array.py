class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        con=0
        dec=False
        inc=False
        if len(nums)<2:
            return True
        if nums[0]>=nums[1]:
            dec=True
        if nums[0]<=nums[1]:
            inc=True
        i=0
       
        while dec and i<len(nums)-1:
            
            if nums[i]<nums[i+1]:
                dec=False
            i+=1
        j=0
        while inc and j<len(nums)-1:
            
            if nums[j]>nums[j+1]:
                inc=False
            j+=1
        
        return inc or dec