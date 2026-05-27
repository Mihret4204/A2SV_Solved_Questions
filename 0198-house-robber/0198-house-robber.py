class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        arr = [-1]*(len(nums))

        def rec(i):
            nonlocal arr
            if i==0:
                return nums[i]
            elif i==1:
                return max(nums[0],nums[i])
            elif arr[i]!=-1:
                return arr[i]
            else:
                arr[i]=max(rec(i-2)+nums[i],rec(i-1))
                return arr[i]
        
        return rec(len(nums)-1)
        

        