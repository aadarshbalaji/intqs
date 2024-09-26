class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numrows = len(grid)
        numcols = len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < numrows) and (0 <= nc < numcols) and (nr,nc) not in visited and grid[nr][nc] == '1':
                        bfs(nr, nc)
                    visited.add((nr,nc))
                q.popleft()


        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        return islands