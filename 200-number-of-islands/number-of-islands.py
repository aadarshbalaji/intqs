class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        lenrows = len(grid)
        lencols = len(grid[0])
        visited = set()
        islands = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(row,col):
            q = deque()
            q.append((r,c))
            visited.add((row,col))
            while q:
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < lenrows and 0 <= nc < lencols and (nr, nc) not in visited and grid[nr][nc] == '1':
                        bfs(nr,nc)
                    visited.add((nr,nc))
                q.popleft()

        for r in range(lenrows):
            for c in range(lencols):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)
                
        return islands