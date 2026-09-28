class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0 
        
        temp = 0
        for c in s:
          
            if c=='(':
                temp+=1
            elif c==')':
                ans = max(temp,ans)
                temp-=1
        return ans
            