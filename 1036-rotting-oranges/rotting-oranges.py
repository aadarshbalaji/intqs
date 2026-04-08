class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        numfresh = 0
        
        q = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    numfresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            if numfresh == 0:
                return time
            time += 1
            for i in range(len(q)):
                currow, curcol = q.popleft()

                for r, c in dirs:
                    nr, nc = currow + r, curcol + c
                    if (0 <= nr < num_rows) and (0 <= nc < num_cols) and grid[nr][nc] == 1:
                        numfresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
        
        return time if numfresh == 0 else -1


