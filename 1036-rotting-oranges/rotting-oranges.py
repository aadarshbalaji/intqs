class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        lenrows = len(grid)
        lencols = len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        for r in range(lenrows):
            for c in range(lencols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            lq = len(q)
            for i in range(lq):
                cr, cc = q.popleft()
                for dr, dc in directions:
                    newrow, newcol = cr + dr, cc + dc
                    if 0 <= newrow < lenrows and 0 <= newcol < lencols and (newrow, newcol) and grid[newrow][newcol] == 1:
                        grid[newrow][newcol] = 2
                        q.append([newrow, newcol])
                        fresh -= 1
            time += 1
        
        return -1 if fresh else time