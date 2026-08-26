class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n =  len(piles)
        suf=[0]*n
        pre = 0
        s=sum(piles)
        for i in range(n):
            suf[i]=s-pre
            pre+=piles[i]

        @cache
        def dp(i,m):
            if i+2*m>=n:
                return suf[i]
            mx=0
            for j in range(1,2*m+1):
                val = suf[i]-dp(i+j,max(m,j))
                mx=max(mx,val)
            return mx


        return dp(0,1)