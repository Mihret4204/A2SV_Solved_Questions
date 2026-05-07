class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        prev=[0]*(n+1)
        mx_prev =  [0]*(n+1)
        adj = [[] for _ in range (n+1)]

        for p,q in relations:
            prev[q]+=1
            adj[p].append(q)
        q= deque()
        for i in range (1,n+1):
            if prev[i] == 0:
                q.append(i)
        
        
        while q:
            curr= q.popleft()
            t = mx_prev[curr]+time[curr-1]

            for nei in adj[curr]:
                prev[nei]-=1
                mx_prev[nei] = max(t,mx_prev[nei])
                if prev[nei]==0:
                    q.append(nei)
        ans=0
        for i in range (1,n+1):
            ans=max(mx_prev[i]+time[i-1],ans)

        return ans