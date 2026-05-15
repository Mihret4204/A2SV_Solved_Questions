class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        ans = (1<<(m-1))*n

        for i in range (1,m):
            val = 1<<(m-1-i)
            count =0

            for j in range (n):
                if grid[j][i] == grid[j][0]:
                    count +=1
            ans+=(max(n-count,count))*val

        return ans