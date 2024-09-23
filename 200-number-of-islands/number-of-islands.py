class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numrows = len(grid)
        numcols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            q = deque()
            visited.add((row,col))
            q.append((r,c))

            while q:
                currow, currcol = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    newrow, newcol = currow + dr, currcol + dc
                    if (newrow, newcol) not in visited and 0 <= newrow < numrows and 0 <= newcol < numcols and grid[newrow][newcol] == '1':
                        q.append((newrow, newcol))
                        bfs(newrow, newcol)


        for r in range(numrows):
            for c in range(numcols):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)
        return islands