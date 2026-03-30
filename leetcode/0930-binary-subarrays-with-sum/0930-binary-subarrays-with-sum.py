class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix=0
        seen={0:1}
        ans=0
        for i in range(len(nums)):
            prefix+=nums[i]
            r=prefix-goal
            if r in seen:
                ans+=seen[r]
            seen[prefix]=seen.get(prefix,0)+1
        return ans

