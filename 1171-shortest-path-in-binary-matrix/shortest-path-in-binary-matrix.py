class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dist = 1
        #visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        q = deque()
        if not grid or grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        q.append((0,0))
        while q:
            lq = len(q)
            for i in range(lq):
                r,c = q.popleft()
                if (r,c) == (n-1,n-1):
                    return dist
                #visited.add((r,c))
                for dr, dc in directions:
                    newrow, newcol = r + dr, c + dc
                    if 0 <= newrow < n and 0 <= newcol < n and (newrow, newcol) and grid[newrow][newcol] == 0:
                        q.append((newrow, newcol))
                        grid[newrow][newcol] = 1
            dist += 1
            
        return -1