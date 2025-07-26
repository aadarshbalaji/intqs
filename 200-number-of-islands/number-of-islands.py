class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numrows = len(grid)
        numcols = len(grid[0])

        def explore(row, col):
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                newrow, newcol = row + dr, col + dc
                if (0 <= newrow < numrows) and (0 <= newcol < numcols) and grid[newrow][newcol] == '1':
                    grid[newrow][newcol] = 'V'
                    explore(newrow, newcol)



        count = 0
        for i in range(numrows):
            for j in range(numcols):
                if grid[i][j] == '1':
                    count += 1
                    explore(i,j)
        return count