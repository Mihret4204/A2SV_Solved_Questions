class Solution:
    def check(self, nums: List[int]) -> bool:
        k=-1
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                k=i
                break
        a=nums[:k+1]
        b=nums[k+1:]
        arr=b+a
        nums.sort()
       
        if nums!=arr:
            return False


            
        return True