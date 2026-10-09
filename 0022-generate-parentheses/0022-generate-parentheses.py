class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        ans = []

        def dp(s,bo,bc):
            if n==bo and bo==bc:
                ans.append(s)
           
            if bc<bo:
                dp(s+')',bo,bc+1)
            if bo<n:
                dp(s+'(',bo+1,bc)
        dp('',0,0)
        return ans