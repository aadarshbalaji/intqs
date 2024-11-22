class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lenrows = len(grid)
        lencols = len(grid[0])
        numfresh = 0
        timer = 0
        directions = [[0,1],[0,-1], [1,0],[-1,0]]
        q = deque()
        for i in range(lenrows):
            for j in range(lencols):
                if grid[i][j] == 1:
                    numfresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        if not numfresh:
            return 0
        while q:
            lq = len(q)
            for i in range(lq):
                row, col = q.popleft()
                for dr, dc in directions:
                    newrow, newcol = row + dr, col + dc
                    if 0 <= newrow < lenrows and 0 <= newcol < lencols and grid[newrow][newcol] == 1:
                        numfresh -= 1
                        grid[newrow][newcol] = 2
                        q.append((newrow, newcol))
            timer += 1
        return -1 if numfresh else timer-1