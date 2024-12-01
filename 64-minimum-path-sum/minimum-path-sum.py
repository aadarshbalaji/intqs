class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = grid
        ans[0][0] = grid[0][0]
        for i in range(1, n):
            ans[0][i] = ans[0][i] + ans[0][i-1]
        for i in range(1, m):
            ans[i][0] = ans[i][0] + ans[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = min(ans[i-1][j], ans[i][j-1]) + grid[i][j]
        return ans[-1][-1]