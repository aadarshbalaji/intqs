class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Defensive check: if grid is empty, there's nothing to do.
    # (LeetCode-style inputs won't hit this, but it keeps the function robust.)
        if not grid or not grid[0]:
            return 0

        # n is the grid dimension (n x n).
        n = len(grid)

        # 'best[r][c]' will store the smallest "max elevation so far" we've found
        # to reach cell (r, c). Initialize to +infinity to mean "unknown/very large".
        INF = float('inf')
        best = [[INF] * n for _ in range(n)]

        # The earliest time we can even stand on the start cell is its own elevation.
        # That is the initial "cost" at (0,0).
        start_cost = grid[0][0]
        best[0][0] = start_cost

        # Min-heap of states to explore.
        # Each item is a tuple (cost, r, c), where 'cost' is the current path's
        # maximum elevation up to (r,c). The heap ensures we always expand the
        # smallest such cost first (Dijkstra's greedy step).
        heap = [(start_cost, 0, 0)]

        # 4-directional movement (up, down, left, right); diagonals are not allowed.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Standard Dijkstra loop: keep exploring the "most promising" cell
        # (smallest cost) until we either finish or exhaust all options.
        while heap:
            # Pop the cell with the minimal "max elevation so far".
            cost, r, c = heapq.heappop(heap)

            # If this popped state is stale (i.e., we've already recorded a better
            # cost for (r,c)), skip it. This is a common optimization in Dijkstra.
            if cost != best[r][c]:
                continue

            # If we've reached the destination, we can stop:
            # Dijkstra guarantees the first pop of (n-1,n-1) is the optimal cost.
            if r == n - 1 and c == n - 1:
                return cost

            # Explore the 4 neighbors of (r,c).
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Stay within bounds of the grid.
                if 0 <= nr < n and 0 <= nc < n:
                    # Moving to (nr,nc) means the path's "max elevation" becomes the
                    # larger of the current path cost and the neighbor's elevation.
                    new_cost = max(cost, grid[nr][nc])

                    # If we've found a route to (nr,nc) with a smaller "max elevation"
                    # than any prior route, record it and push it for exploration.
                    if new_cost < best[nr][nc]:
                        best[nr][nc] = new_cost
                        heapq.heappush(heap, (new_cost, nr, nc))

        # In a valid problem setup, we should always return inside the loop when
        # we pop the destination. This return is just a fallback.
        return -1