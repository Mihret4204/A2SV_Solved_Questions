class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            return 0

        _map=defaultdict(list)
        for i in range (n):
            _map[arr[i]].append(i)
        q=deque()
        visited=set()
        q.append((0, 0))
        visited.add(0)

        while q:
            node, ans = q.popleft()
            if node==n-1:
                return ans
            
            a=_map[arr[node]]
            if node+1<n:
                a.append(node+1)
            if node-1>=0:
                a.append(node-1)

            for nei in a:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, ans+1))
            _map[arr[node]].clear()
        
        return -1
            