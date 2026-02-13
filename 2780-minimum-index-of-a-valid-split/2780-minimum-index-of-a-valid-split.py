from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        total =Counter(nums)
        left_cnt=0
        num_max,cnt_max =max(total.items() ,key=lambda p:p[1])
        right_cnt=cnt_max
        for i in range(len(nums)-1):
            if nums[i]==num_max:
                #left count->if we add it ti lft arr
                left_cnt+=1
                right_cnt-=1
            
            if left_cnt*2>i+1 and right_cnt*2>(len(nums)-i-1):
                return i
        return -1