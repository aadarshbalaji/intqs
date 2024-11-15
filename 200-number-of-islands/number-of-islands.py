class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numrows = len(grid)
        numcols = len(grid[0])
        total = 0
        visited = set()
        def search(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                currR, currC = q.popleft()
                for dr, dc in directions:
                    newR, newC = currR + dr, currC + dc
                    if 0 <= newR < numrows and 0 <= newC < numcols and grid[newR][newC] == '1' and (newR,newC) not in visited:
                        q.append((newR,newC))
                        visited.add((newR,newC))


        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    total += 1
                    search(r,c)
        return total