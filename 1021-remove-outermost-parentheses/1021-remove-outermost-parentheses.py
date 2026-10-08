class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        temp = 0
        for c in s:
            if c==')':
                temp-=1
            if temp>0:
                ans.append(c)
            if c=='(':
                temp+=1
            
                
        return "".join(ans)