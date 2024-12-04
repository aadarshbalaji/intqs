class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        maxlen = 0 
        for x in range(len(matrix)):
            dp[x][0] = 1 if matrix[x][0] == '1' else 0
            maxlen = max(maxlen ,dp[x][0])
        for x in range(len(matrix[0])):
            dp[0][x] = 1 if matrix[0][x] == '1' else 0
            maxlen = max(maxlen ,dp[0][x])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                maxlen = max(maxlen, dp[i][j])
        return maxlen * maxlen
                

                