class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        l=n//2
        costs=sorted(costs, key=lambda z: z[1]-z[0])
        total=0
        for i in range(l):
            total+=costs[i][1]
        for i in range(l,n):
            total+=costs[i][0]
           
        return total


