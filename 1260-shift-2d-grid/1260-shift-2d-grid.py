class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        c =  len(grid[0])
        n = r*c
        k = k%n

        if not k: return grid

        ans  = [[0]* c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                x = ((i*c +j)+k) % n
                ans[x//c][x%c]= grid[i][j]
       
        return ans
                
            

