class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        arr = [0]*numCourses
        
        for p,q in prerequisites:
            graph[q].append(p)
            arr[p]+=1
        q=deque()
        ans=[]
        for i in range(numCourses):
            if arr[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            ans.append(node)

            for nei in graph[node]:
                arr[nei]-=1
                if arr[nei]==0:
                    q.append(nei)
        if len(ans)!=numCourses:
            return []
        return ans