class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i,num in enumerate(nums):
            match =target -num
            if match in store:
                return [store[match ],i]
            store[num]=i
        return []