class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        graph = defaultdict(list)
        n=len(arr)
        for i in range (n):
            if i-arr[i]>=0:
                graph[i].append(i-arr[i])
            if i+arr[i]<n:
                graph[i].append(i+arr[i])
       
        q =  deque()
        q.append(start)
        visited=set()
        while q:
            
            
            node=q.popleft()
            if node in visited:
                return False
            if arr[node]==0:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if arr[nei]==0:
                        return True
                    q.append(nei)

        return False
