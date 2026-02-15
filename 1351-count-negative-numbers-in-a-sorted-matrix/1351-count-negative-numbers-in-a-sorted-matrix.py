class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range (cols):
                if grid[i][j]<0:
                    count+=cols-j
                    break


        return count