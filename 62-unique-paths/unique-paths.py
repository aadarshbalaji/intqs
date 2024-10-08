class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for j in range(m):
            dp[j][0] = 1
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[m-1][n-1]