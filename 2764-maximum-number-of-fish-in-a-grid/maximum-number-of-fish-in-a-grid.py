class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        lenrows = len(grid)
        lencols = len(grid[0])
        currmax = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isvalid(testrow, testcol):
            return 0 <= testrow < lenrows and 0 <= testcol < lencols and grid[testrow][testcol] > 0

        def explore(row, col, visited):
            if not isvalid(row, col) or (row, col) in visited:
                return 0
            visited.add((row, col))
            fish_count = grid[row][col] 
            for dr, dc in directions:
                fish_count += explore(row + dr, col + dc, visited)
            
            #visited.remove((row, col)) 
            return fish_count

        for r in range(lenrows):
            for c in range(lencols):
                if grid[r][c] > 0:  # Only start DFS if it's a water cell
                    currmax = max(currmax, explore(r, c, set()))

        return currmax