class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lenrows = len(grid)
        lencols = len(grid[0])
        numfresh = 0
        timer = 0
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        q = deque()
        for i in range(lenrows):
            for j in range(lencols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    numfresh += 1

        if numfresh == 0:
            return 0
        
        while q:
            if numfresh == 0:
                return timer
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < lenrows and 0 <= nc < lencols and grid[nr][nc] == 1:
                        numfresh -= 1
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            timer += 1
        return -1