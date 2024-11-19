class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lenrows = len(grid)
        lencols = len(grid[0])
        count = 0
        numfresh = 0
        q = deque()
        for r in range(lenrows):
            for c in range(lencols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    numfresh += 1
        if numfresh == 0:
            return 0
        while q:
            print(q)
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[0,1], [0,-1],[-1, 0], [1,0]]:
                    newrow, newcol = row + dr, col + dc
                    if not 0 <= newrow < lenrows or not 0 <= newcol < lencols or grid[newrow][newcol] != 1:
                        continue
        
                    q.append((newrow, newcol))
                    grid[newrow][newcol] = 2
                    numfresh -= 1
            count += 1
        return -1 if numfresh > 0  else count - 1