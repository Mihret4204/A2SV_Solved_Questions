class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans=0
        prefix=0

        for n in nums:
            prefix+=n
            ans=min(ans,prefix)
        return 1-ans