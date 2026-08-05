class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        visited = set()
        store= defaultdict(list)

        for a , b in edges:
            store[a].append(b)
            store[b].append(a)
        
        

        def dfs(node,visited):
            if node==destination:
                return True
            visited.add(node)

            for nei in store[node]:
                if nei not in visited:
                    if dfs(nei,visited):
                        return True
            return False 

        return dfs(source,visited)