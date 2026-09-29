class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        ans = n + 1
        l = 0
        tot = 0
        dp = [n+1]*(n+1)

        for i in range(n):
            tot+=arr[i]

            while tot>target:
                tot-=arr[l]
                l+=1
            dp[i+1]=dp[i]
            if tot==target:
                ans = min(ans,dp[l]+i-l+1)
                dp[i+1]=min(dp[i],i-l+1)
        if ans==n+1:
            return -1
        return ans



        
