class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = 1
        for i in range(1,len(nums)):
            if nums[i-1] +1 != nums[i]:
                l = i
                break
            l+=1
      
        s = sum(nums[:l])
        m =  max(nums)
        while s < m:
            if s not in nums:
                return s
            s+=1
        if s not in nums:
            return s
        else:
            return s+1