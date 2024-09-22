class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        numrows, numcols = len(grid), len(grid[0])

        def bfs(crow, ccol):
            q = deque()
            visited.add((crow, ccol))
            q.append((crow,ccol))
            while q:
                lrow, lcol = q.popleft()
                directions = [[0,1], [0,-1],[1,0], [-1,0]]
                for dr, dc in directions:
                    nr, nc = lrow + dr, lcol + dc
                    if 0 <= nr < numrows and 0 <= nc < numcols and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))


        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        return islands