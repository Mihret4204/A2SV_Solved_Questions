class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        prev_end = float('-inf')
        count=0
        for i in range(len(points)):
            start=points[i][0]
            end=points[i][1]
            if start>prev_end:
                count+=1
                prev_end=end
        return count

            
             