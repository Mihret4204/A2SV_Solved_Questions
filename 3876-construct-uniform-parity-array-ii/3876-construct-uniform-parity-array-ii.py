class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        s = float('inf')
        for num in nums1:
            if num%2==1:
                s=min(s,num)
        if s ==  float('inf'):
            return True
        for num in nums1:
            if num%2==0 and num<=s:
                return False
        return True