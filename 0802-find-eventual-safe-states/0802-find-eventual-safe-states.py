class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        arr = [0]*(len(graph))
    
        def dfs(node):
            if arr[node]==1:
                return False

            arr[node]=1
            for nei in graph[node]:
                if arr[nei]==2:
                    continue 
                if not dfs(nei):
                    return False
            arr[node]=2
            ans.append(node)
            return True
            

        for i in range (len(graph)):
            if arr[i]!=0:
                continue 
            dfs(i)
        ans.sort()
        return ans
