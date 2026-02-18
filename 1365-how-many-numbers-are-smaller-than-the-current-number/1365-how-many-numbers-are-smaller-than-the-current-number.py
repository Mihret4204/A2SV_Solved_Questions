class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mapping ={}
        sorted_nums=sorted(nums)
        for idx,val in enumerate(sorted_nums):
            if val not in mapping:
                mapping [val]=idx
        return [mapping[i] for i in nums]