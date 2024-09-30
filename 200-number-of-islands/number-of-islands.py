class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lenrows = len(grid)
        lencols = len(grid[0])
        islands = 0
        visited = set()
        def search(row, col):
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = row  + dr, col + dc
                    if 0 <= nr < lenrows and 0 <= nc < lencols and (nr, nc) not in visited and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        search(nr,nc)

        for r in range(lenrows):
            for c in range(lencols):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    search(r,c)
        return islands