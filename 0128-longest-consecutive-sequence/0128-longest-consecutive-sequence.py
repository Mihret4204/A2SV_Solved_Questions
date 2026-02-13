class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        curr=1
        longest=1
        if not nums:
            return 0
        for n in nums_set:
            curr=1
            if n-1 not in nums_set:
                curr_num=n
                while n+1 in nums_set:
                    curr+=1
                    n+=1
                longest =max(curr,longest)
                    
        return longest


        