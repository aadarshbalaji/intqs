class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = collections.deque()
        mins = 0
        numoranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    numoranges += 1
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            
            if numoranges <= 0:
                break
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        numoranges -= 1
                        grid[nr][nc] = 4
            mins += 1
            #print(grid)
        if numoranges == 0:
            return mins
        else:
            return -1
