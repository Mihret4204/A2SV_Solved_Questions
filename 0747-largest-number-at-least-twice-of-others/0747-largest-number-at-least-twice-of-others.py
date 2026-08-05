class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        numb = nums[:]
        numb.sort()
        if numb[-1]>= 2*(numb[-2]):
            idx = nums.index(numb[-1])
            return idx
        return -1