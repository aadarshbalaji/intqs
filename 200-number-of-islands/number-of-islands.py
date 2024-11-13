class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lenrows = len(grid)
        lencols = len(grid[0])
        count = 0
        visited = set()

        def search(orow, ocol):
            if (orow, ocol) in visited:
                return
            visited.add((orow,ocol))
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr, dc in dirs:
                newrow, newcol = orow + dr, ocol + dc
                if 0 <= newrow < lenrows and 0 <= newcol < lencols and grid[newrow][newcol] == '1':
                    search(newrow, newcol)
                    visited.add((newrow, newcol))  

            
                          



        for r in range(lenrows):
            for c in range(lencols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    search(r, c)
        return count