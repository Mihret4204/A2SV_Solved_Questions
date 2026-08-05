class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        i =0
        ans = []
        nums.sort()
        while i<  (len(nums)) - 1:
            if nums[i] != nums[i+1]:
                ans.append(nums[i])
                i-=1
            i+=2
        if len(ans)<2:
            ans.append(nums[-1])
        return ans

    