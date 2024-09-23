class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        lenrows, lencols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                directions = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < lenrows and 0 <= nc < lencols and (nr, nc) not in visited and grid[nr][nc] == '1':
                        #q.append((nr,nc))
                        bfs(nr,nc)
                    visited.add((nr,nc))
                q.popleft()


        for row in range(lenrows):
            for col in range(lencols):
                if (row, col) not in visited and grid[row][col] == '1':
                    islands += 1
                    bfs(row,col)
        return islands