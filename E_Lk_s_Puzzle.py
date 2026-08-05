import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y, px, py, color):
    if visited[x][y]:
        return True
    
    visited[x][y] = True
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] != color:
                continue
            if nx == px and ny == py:
                continue
            
            if dfs(nx, ny, x, y, color):
                return True
    
    return False
con=False
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, -1, -1, grid[i][j]):
                con=True
                break
    if con:
        break
if con:
    print("Yes")
else:           
    print("No")