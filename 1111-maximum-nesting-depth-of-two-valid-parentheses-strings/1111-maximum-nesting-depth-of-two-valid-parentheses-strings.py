class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        x = 0
        for c in seq :
            if c == '(':
                x+=1
                ans.append(x%2)
            if c == ')':    
                ans.append(x%2)
                x-=1
        return ans