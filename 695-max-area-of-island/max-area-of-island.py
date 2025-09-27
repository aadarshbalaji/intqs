class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currmax = [0]
        numrows = len(grid)
        numcols = len(grid[0])
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(row, col):
            area = 1
            visited.add((row,col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < numrows and 0 <= nc < numcols and (nr,nc) not in visited and grid[nr][nc] == 1:
                    area += dfs(nr,nc)
            return area
        
        for i in range(numrows):
            for j in range(numcols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    currmax[0] = max(currmax[0], dfs(i,j))
        
        return currmax[0]