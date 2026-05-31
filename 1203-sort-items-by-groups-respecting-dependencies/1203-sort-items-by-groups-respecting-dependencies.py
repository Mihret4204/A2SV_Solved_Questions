class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId+=1
        
        groupGraph = defaultdict(list)
        groupIndegree = [0] * groupId
        itemGraph =defaultdict(list)
        itemIndegree = [0] * n

        for i in range(n):
            for item in beforeItems[i]:
                itemGraph[item].append(i)
                itemIndegree[i] += 1
                if group[item] != group[i]:
                    groupGraph[group[item]].append(group[i])
                    groupIndegree[group[i]]+=1
        
        

        orderItem = self.topSort(itemGraph, itemIndegree)
        orderGroup = self.topSort(groupGraph, groupIndegree)

        if not orderGroup or not orderItem:
            return []

        orderedGroup = defaultdict(list)
        for item in orderItem:
            orderedGroup[group[item]].append(item)
        ans = []
        for item in orderGroup:
            ans.extend(orderedGroup[item])
        return ans 
        


    def topSort(self, graph: Dict[int, List[int]], indegree: List[List[int]]):
        visited = []
        stk = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                stk.append(i)

        
        while stk:
            curr =  stk.pop()
            visited.append(curr)

            for elt in graph[curr]:
                indegree[elt]-=1
                if indegree[elt] ==0 :
                    stk.append(elt)
                    
        
        if len(visited)==len(indegree):
            return visited
        return []
