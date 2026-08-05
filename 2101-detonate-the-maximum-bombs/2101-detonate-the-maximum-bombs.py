class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len (bombs)
        adj =[[] for _ in range (n)]
        for i in range(n):
            for j in range (n):
                if i == j : continue
                r=bombs[i][2]
                #print((bombs[i][0] - bombs[j][0])**2 +(bombs[i][1] - bombs[j][1])**2)
                if ((bombs[i][0] - bombs[j][0])**2 +(bombs[i][1] - bombs[j][1])**2)<=r**2:
                    adj[i].append(j)
        
        def dfs(j,visited):
            for c in adj[j]:
                if c not in visited:
                    visited.add(c)
                    dfs(c,visited)
             

        ans=0
        for i in range (n):
            visited= set([i])
            dfs(i,visited)
            ans=max(ans,len(visited))
        
        return ans