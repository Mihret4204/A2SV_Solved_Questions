class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(graph)-1
        def dfs(num,arr):
            if num==n:
                ans.append(arr[:])
                return 
            for nei in graph[num]:
                arr.append(nei)
                dfs(nei,arr)
                arr.pop()
        

        dfs(0,[0])
        return ans