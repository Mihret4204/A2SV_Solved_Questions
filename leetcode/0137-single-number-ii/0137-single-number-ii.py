class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = sum(set(nums))*3
        a = sum(nums)

        return (s-a)//2