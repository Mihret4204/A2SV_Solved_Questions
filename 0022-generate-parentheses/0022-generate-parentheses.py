class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(st, op, cl):

            if op == n and cl == op:
                ans.append(st)
               
            if op < n:
               
                dfs(st+"(",op+1,cl)
            if op > cl:
               
                dfs(st+")", op, cl+1)
            

             
        dfs("",0,0)
        return ans