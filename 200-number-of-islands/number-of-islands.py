class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lenrows = len(grid)
        lencols = len(grid[0])
        islands = 0
        visited = set()

        def bfs(row, col):
            q = deque()
            visited.add((row,col))
            q.append((row,col))
            while q:
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
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