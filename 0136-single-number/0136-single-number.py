class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set=set()
        for c in nums:
            my_set.add(c)
        ans=2*(sum(my_set))-sum(nums)
        return ans       