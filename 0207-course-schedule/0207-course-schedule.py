class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=defaultdict(list)

        for a,b in prerequisites:
            pre[a].append(b)
        taken=set()
        def dfs(course):
            
            if not pre[course]:
                return True
            if course in taken:
                return False
                
            taken.add(course)

            for c in pre[course]:
                dfs(c)
                if not dfs(c):
                    return False
            pre[course]=[]
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True