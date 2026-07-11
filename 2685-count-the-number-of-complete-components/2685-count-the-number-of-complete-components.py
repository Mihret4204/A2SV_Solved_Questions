class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        _map =  defaultdict(list)
       
        arr = [0]*n
        for a,b in edges:
            _map[a].append(b)
            _map[b].append(a)
            
        ans = 0
        visited =  set()

        def dfs(node, comp):
            comp.add(node)
            visited.add(node)
            for nei in _map[node]:
                if nei not in visited:
                    dfs(nei,comp)

        for i in range(n):
            con = True
            if i not in visited:
                comp = set()
                dfs(i,comp)
                for node in comp:
                    if len(_map[node])!=len(comp)-1:
                        con=False
                        break
                if con:
                    ans+=1
                        
       

        return ans