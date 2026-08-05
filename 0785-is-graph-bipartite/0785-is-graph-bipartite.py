class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       
        n=len(graph) 
        color = [0]*n
        
        for i in range(n):            
            if color[i]!=0:
                continue 
            q=deque()
            q.append(i)
            color[i]=1

            while q:
                node=q.pop()
                for nei in graph[node]:
                    if color[nei]==0:
                        color[nei] = -color[node]
                        q.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True
        
        