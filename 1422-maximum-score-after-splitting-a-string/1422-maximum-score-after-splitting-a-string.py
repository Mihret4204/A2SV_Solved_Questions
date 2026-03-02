class Solution:
    def maxScore(self, s: str) -> int:
        l=0
        r=0
        ans=0
        for i in range(len(s)):
            if s[i]=='1':
                r+=1 
        for i in range (len(s)-1):
            if s[i]=='0':
                l+=1
            else:
                r-=1
            score=r+l
            ans=max(score,ans)
        return ans
        