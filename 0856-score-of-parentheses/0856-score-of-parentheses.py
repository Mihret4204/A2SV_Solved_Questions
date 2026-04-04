class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0
        stack=[]
        

        for c in s:
            
            if c=='(':
                stack.append(ans)
                ans=0
            else:
                ans=ans+stack.pop()+max(ans,1)
            
        return ans
            
