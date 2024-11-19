class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        n = primeOne * primeTwo
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i] == True:
                if (i + primeOne) < n:
                    dp[i + primeOne] = True
                if (i + primeTwo) < n:
                    dp[i + primeTwo] = True
        
        for i in range(n-1, -1, -1):
            if not dp[i]:
                return i