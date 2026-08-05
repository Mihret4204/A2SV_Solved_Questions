class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mxi = nums[0]
        pre_arr = []
        n = len(nums)
        for i in range (n):
            if mxi < nums[i]:
                mxi = nums[i]
            
            pre_arr.append(gcd(mxi,nums[i]))
        pre_arr.sort()
        arr = []
        for i in range(n//2):
            arr.append(gcd(pre_arr[i],pre_arr[n-i-1]))    
        
        return sum(arr)