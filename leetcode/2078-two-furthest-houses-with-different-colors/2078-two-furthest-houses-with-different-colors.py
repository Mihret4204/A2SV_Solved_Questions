class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)-1
        ans=0

        for i in range(n+1):
            if colors[i]!=colors[0]:
                ans=max(ans,i)
            if colors[i]!=colors[n]:
                ans=max(ans,n-i)
        return ans