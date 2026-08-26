class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = 0
        mx = max(nums)
        y = mx//k + 1
        for i in range (1,y):
            if i*k not in nums:
                return i*k
        return y*k