class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)

        for u,v in edges:
            graph[v].append(u)
        
        def dfs(i, visited):
            for v in graph[i]:
                if v not in visited:
                    visited.add(v)
                    dfs(v, visited)

        ans=[]
        for i in range (n):
            visited=set()
            dfs(i,visited)
            ans.append(sorted(visited))
        return ans