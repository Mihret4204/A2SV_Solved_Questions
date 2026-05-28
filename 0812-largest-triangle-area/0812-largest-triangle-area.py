class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        n=len(points)
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    area =  1/2 *(abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1]- points[j][1])))
                    ans=max(ans,area)
        return ans