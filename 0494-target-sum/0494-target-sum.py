class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        ans = 0
        self.memo = {}
        return self.dp(nums, n, target, ans)
    def dp(self, nums,idx,target,curr):
        if (idx,curr) in self.memo:
            return self.memo[(idx, curr)]
        if idx < 0 and curr==target:
            return 1
        if idx<0:
            return 0
        pos = self.dp(nums,idx-1,target,curr+ nums[idx])
        ne = self.dp(nums,idx-1,target,curr-nums[idx])

        self.memo[(idx, curr)] = pos + ne
        return pos+ne
